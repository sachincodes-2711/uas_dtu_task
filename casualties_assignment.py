import numpy as np
import math
import cv2 as cv

CAMP_CAPACITIES = {
    "Pink": 3,
    "Blue": 4,
    "Grey": 2
}


CITIZEN_PRIORITY_MAP = {"Child": 3, "Elder": 2, "Adult": 1}
EMERGENCY_PRIORITY_MAP = {"Severe": 3, "Mild": 2, "Safe": 1}


def calculate_distance(p1, p2):
    return math.sqrt((int(p1[1]) - int(p2[1])) ** 2 + (int(p1[0]) - int(p2[0])) ** 2)


def assign_casualties(casualties, camps, img):
    """
    casualties: List of dicts {'id': 0, 'loc': (x,y), 'type': 'Child', 'severity': 'Severe'}
    camps: List of dicts {'color': 'Pink', 'loc': (x,y), 'assigned': []}
    """
    for cas in casualties:
        p_type = CITIZEN_PRIORITY_MAP.get(cas['type'])
        em_prio = EMERGENCY_PRIORITY_MAP.get(cas['severity'])

        cas['priority_score'] = p_type * em_prio
        cas['raw_p_type'] = p_type
        cas['raw_em_prio'] = em_prio

    # 2. Sort Casualties
    # Strategy: High Priority gets first choice of the closest camp.
    # Sort by Priority Score (Desc), then Emergency Score (Desc) as tie-breaker.
    def assignment_order(casualties):
        return (casualties['priority_score'], casualties['raw_em_prio'])

    sorted_casualties = sorted(casualties, key=assignment_order, reverse=True)



    # 3. Assignment Logic
    for cas in sorted_casualties:
        best_camp = None
        min_score = float('inf')  # We want to minimize distance for the high priority targets

        for camp in camps:
            camp_name = camp['color']

            # Check Capacity
            if len(camp['assigned']) < CAMP_CAPACITIES.get(camp_name, 0):
                dist = calculate_distance(cas['loc'], camp['loc'])

                score = dist

                if score < min_score:
                    min_score = score
                    best_camp = camp

        if best_camp:
            best_camp['assigned'].append(cas)
            print(f"Assigned {cas['type']} ({cas['severity']}) to {best_camp['color']} Camp. (Dist: {min_score:.2f})")

            # drwaing arrows
            cv.arrowedLine(img, cas['loc'], best_camp['loc'], (0,0,255), 2)
        else:
            print(f"CRITICAL: No space left for {cas['type']} at {cas['loc']}")



    return camps, img


def calculate_rescue_ratio(camps, total_casualties_count):
    total_priority_sum = 0

    print("\n--- CAMP TOTALS ---")
    for camp in camps:
        camp_sum = sum(c['priority_score'] for c in camp['assigned'])
        total_priority_sum += camp_sum
        print(f"{camp['color']} Camp Total Score: {camp_sum}")

    rescue_ratio = total_priority_sum / total_casualties_count if total_casualties_count > 0 else 0
    print(f"Rescue Ratio (Pr): {rescue_ratio:.2f}")
    return rescue_ratio
