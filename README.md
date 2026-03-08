# EngHack Project

## Problem Statement

In winter, **Seasonal Affective Disorder (SAD)** is a common mental health issue. It is a type of depression with symptoms such as persistent sadness, hopelessness, and anxiety [1].

In Canada, about **15% of people experience mild SAD** during their lifetime, while **2–3% experience severe cases** [2]. Research shows that **reduced sunlight exposure during winter** is one of the primary causes of SAD because it disrupts circadian rhythms. Cold weather and reduced outdoor activity can also contribute to the condition [3][4].

If untreated, SAD can significantly affect daily functioning and, in severe cases, may lead to **suicidal thoughts or behaviors**, highlighting the importance of early monitoring and intervention [5].

---

## Brainstorming

We developed our solution by identifying common causes of Seasonal Affective Disorder. We found that **insufficient light exposure** and **unsuitable indoor temperature** can contribute to depression and anxiety during winter. Therefore, we designed a system that **automatically adjusts these environmental conditions** to help reduce the risk of SAD.

We also recognized that improving a room’s environment may involve more than just temperature and light. As a result, the system can provide **personalized recommendations** based on different combinations of environmental factors.

During brainstorming, we considered several other ideas:

1. **Anti-tripping systems**
2. **Snow depth and obstacle detection**
3. **Electronic body temperature measurement machine**

The first two ideas were rejected because they would require installation on crutches and might duplicate existing assistive technologies. The third idea was dismissed due to concerns about **uncertainty and limited experimental data**.

---

## Solution

Our solution is a **smart environmental monitoring and adjustment system** designed to reduce the risk of Seasonal Affective Disorder.

The device scans the entire window area and continuously monitors **light intensity and room temperature**. It rotates **360 degrees** to collect environmental data in real time.

Based on the recorded data, the system performs analysis using:

- Time-series analysis  
- Multivariate regression  
- AI-based data processing  
- Big data modeling  

The system then **automatically adjusts indoor lighting** and provides feedback on how to improve the local environment.

This solution is especially helpful for **elderly or disabled individuals**, particularly when a caretaker is not present.

---

## Accessibility Features

To ensure the device is usable by people with different needs, the system includes several accessibility features:

- **Large-text display**
- **High-contrast interface**
- **Support for homes without WiFi**
- **Simple button-based interaction**

Users can press a button to immediately adjust temperature and lighting. The system will **record these preferences and incorporate them into future environmental analysis**, allowing personalized comfort settings.

---

## Future Improvements

We plan to expand the system with additional features, including:

- **Enhanced database integration and personalization**, enable training personal model in different room environment and personalize the parameters and threshold contributing the output.
- **Voice functionality** to read LCD information aloud
- **Automatic temperature adjustment**
- **Mobile base with object detection** to allow the device to move and collect data across an entire building or apartment
- **Enhanced IoT integration**, enabling automatic control of room lighting and temperature without requiring user interaction


These improvements will further enhance accessibility and make the system more helpful for **elderly individuals and people with limited mobility**.

---

## References

[1] https://www.nimh.nih.gov/health/publications/seasonal-affective-disorder  

[2] https://cpa.ca/psychology-works-fact-sheet-seasonal-affective-disorder-depression-with-seasonal-pattern/  

[3] https://sncs-prod-external.mayo.edu/hometown-health/featured-topic/recognizing-seasonal-affective-disorder-sad  

[4] https://www.hopkinsmedicine.org/health/conditions-and-diseases/seasonal-affective-disorder  

[5] https://www.nimh.nih.gov/health/publications/seasonal-affective-disorder