# Bluecoats - A Human-Centric Measurement and Response Program
* **Description**: Bluecoats is a closed-loop, human-centric measurement and response program coordinating training, resources, and operational mechanisms to empower health system staff and management to systematically diagnose issues and develop custom solutions that improve employee wellbeing, streamline operations, and bolster the financial health of the organization.
* **Role**: *Lead Data Scientist* allocated to the Blucoats program
  * **Responsibilities**: Ideation, design, development, implementation, maintenance, and documentation of dedicated processes for:
    * **Opportunity Discovery**: *Analyze enterprise-wide SCORE survey responses* on workplace satisfaction and wellbeing to identify high-opportunity work settings, uits, and positions
    * **Problem-Space Characterization**: *Analyze multi-stage, employee engagement survey responses*, including numerical and free-text data, to surface recurring issues and operational inefficiencies
    * **Project Selection**: *Analyze employee-driven "budgeting exercise" data* to identify the most salient issues for cross-functional project development and implmentation
    * **Project Evaluation**: *Analyze project-specific outcomes* and develop metrics to evaluate project efficacy via historical operational benchmarks, identify areas for further invetigation, and apply root cause analysis as needed
    * **Program Evaluation**: *Analyze collective program outcomes* and develop metrics to evaluate program efficacy via the impact of Bluecoats engagement, communiction, advocacy, and direct actions on employee feelings of hope, trust, and belonging.
    * **Program Expansion**: *Transform analytical results and vizualizations* into an accessible, compelling narrative that inspires key stakeholders and executive leadership to expand the program scale, scope, and span of influence across the University of Pennsylvania Health System.

---

## Select Program Outcomes

---

### Program Expansion - Implementation Architecture Proposal
![Implementation Architecture](resources/phase2_proposed_implementation_architecture.png)

---

### Opportunity Discovery - SCORE Survey
![Difference in Average Percent Positive Responses: Work Settings vs Entity by SCORE Question](output/figures/score_ws_qid_pct_pos_20230328.png)
![Difference in Average Percent Positive Responses: Nurse Work Settings vs Entity by SCORE Question](output/figures/score_nurse_qid_pct_pos_20230330.png)
![Difference in Average Percent Positive Responses: ER Positions vs Entity by SCORE Question](output/figures/score_er_qid_pct_pos_20230330.png)

---

### Problem-Space Characterization - Employee Engagement
![Employee Engagement: Survey 1](output/figures/engagement_survey1_results_20230417.png)
![Employee Engagement: Survey 2](output/figures/engagement_survey2_results_20230429.png)

---

### Project Selection - Budgeting Exercise
![Budgeting Exercise Results: Presby ED](output/figures/budgeting_exercise_results_20230510.png)

---

### Project Evaluation - Supplies Project
* A recurring issue raised by ED staff, especially nurses, was the difficulty in keeping supply carts stocked both across shifts and during busy periods within shifts; there are two supply closets in the ED at this facility that require swiping an ID card for access.
  * I asked for supply closet swipe data to explore this issue. This was the state of the *raw supply closet swipe data*:
![Raw Supply Closet Swipe Data](resources/phase1_roi_examples/supply_room_raw.png)
* The **first opportunity** in the *Supplies Project* was to transform this data into a digestible format; the *Chief ED Security Official* was also highly supportive of this endeavor!
  * I identifyed patterns within the noise and reformatted the raw supply closet swipe data into *master supply closet swipe data*:
![Master Supply Closet Swipe Data](resources/phase1_roi_examples/supply_room_master.png)
* With clean, validated data, I was able to calculate the total number of access events, the number of access events per employee, and the number of access events over varying increments of time, among other things.
  * I was then able to calculate various estimates for the "monthly deadweight loss" incurred when searching for scarce, disorganized supplies by combining this data with research studies estimating the average amount of time ED staff spend looking for supplies (**Note**: No memeber of the ED staff was responsible for organizing the supply closets - these estimates are purely due to *operational inefficiencies*, **not** ED staff negligence.):  
![Supplies ROI Example](resources/phase1_roi_examples/supplies_roi_example.png)
  * I was also able to perform an in-depth analysis of supply closet utilization across a number of operational dimensions, such as *day of week* and *day vs night shift*, as demonstrated below (many more such examples can be seen in the corresponding jupyter notebook):
![Daily Supply Closet Access Events Aggregated by Day of Week and Shift](output/figures/access_events_dayofweek_shift_20230712.png)
* The **second opportunity** in the *Supplies Project* was to **1)** identify appropriate ED leadership on behalf of the ED staff and **2)** successfuly advocte for a new ED staff position dedicated to keeping supply carts stocked at all times. *The response of the ED staff after the first week was overwhelmingly positive*, both in terms of operational efficiency and workplace wellbeing. Problem solved? Not quite.
  * In a follow-up analysis of supply closet access events over time, hoping to see either a reduction in access events or a substantial shift from general ED staff to the dedicated ED staff member, I noticed something quite peculiar in the data instead - one of the supply closets seemed to stop being used at all!:
![Daily Supply Closet Access Events Parallel Coordinates Plot](output/figures/access_events_parallel_coords_20230728.png)
![Daily Supply Closet Access Events Time Series](output/figures/access_events_time_series_20230802.png)
* ED staff did not mention the defective scanner despite repeatedly brigning up stocking supply carts as a major issue. The **root problem** only became apparent in the data after the dedicated ED staff member started *tying the supply door open* to avoid unecessary delays while supporting the ED staff. 
* Thus, the **third and final opportunity** in the *Supplies Project* was the identification and replacement of a defective supply closet scanner that had caused **tens of thousands of dollars in monthly losses!** and **was resolved in one day at negligible cost**.

---

### Program Evaluation - Hope, Trust, and Belonging
* The staff-centered, data-driven approach of the Bluecoats Program was a momumental success that is clearly demonstrated both in the final program evaluation report and the enthusiastic expansion of the program to other departments across the health system:
![ED Staff Feelings Stratified by Bluecoats Actions](output/figures/feelings_actions_20230824.png)
![Bluecoats Actions Stratified by ED Staff Feelings](output/figures/actions_feelings_20230824.png)
![Clustermap of Bluecoats Actions Correlated with ED Staff Feelings](output/figures/actions_feelings_corr_20230824.pdf)
* **Note**: The final clustermap visualizing the *correlation between Bluecoats actions and ED staff feelings* naturally structured the Bluecoats actions - engaging, communicating, advocating, and taking-action - *in the order that they were executed throughout the program lifecycle!* What's more, you can also see a corresponding, positively-sloped correlation structure mapping sequential Bluecoats actions to increasingly powerful single and composite feelings experienced by the ED staff! Oh, and if you look carefully at *any* of the three figures above, we have reinforced, yet again, that *communication builds trust*. 


