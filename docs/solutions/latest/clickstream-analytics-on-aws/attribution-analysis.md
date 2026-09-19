---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/attribution-analysis.html
---

# Attibution Analysis
<a name="attribution-analysis"></a>

 Attribution analysis is an analytics technique to assign credit to the touchpoint in user conversion journeys for a conversion goal. It allows you to understand the importance of different touchpoints for a specific goal in your website and apps.

## Use cases
<a name="use-cases-5"></a>

 Attributions analysis are commonly used when analyzing the contribution of specific touchpoints, for example:
+ Identify the most important promotion slots within an app/website in terms of their contribution to a purchase goal;
+  Identify the most important traffic channels for an app/website based on the contribution to a conversion goal.

## Key concept
<a name="key-concept-2"></a>
+  **Conversion goal:** A quantifiable metric that the app owner wants to achieve, e.g., number of purchase, purchase value, registration user number.
+  **Touchpoint**: Events that app owner designed in the user journey to drive user towards the conversion goal, e.g., page\_view, product exposure, button\_click.
+  **Attribution models**: Attribution models are a set of rules or data-driven algorithms used to determine how conversions are assigned to touchpoints on the conversion path. There is no one-fits-all model, choose one base on your scenario. Clickstream Analytics on AWS supports the following models:

<table>
<thead>
  <tr><th> <b>Models</b> </th><th> <b>Definition</b> </th><th>Applicable scenerio</th><th>Consideration</th></tr>
</thead>
<tbody>
  <tr><td>First-Touch Attribution </td><td>The first attribution touchpoint in completing a goal event receives 100% contribution.</td><td>For example, in the early testing phase of the homepage flash sales, the initial traffic source plays the most important roles.</td><td>Amplifies the value of the traffic source, underestimates the output of other touchpoints.</td></tr>
  <tr><td>Last-Touch Attribution </td><td>The last attribution touchpoint in completing a goal event receives 100% contribution.</td><td>Helps understand which touchpoint led to the final decision for a transaction.</td><td>May underestimate certain touchpoints that are not closed to conversion event, but avoids the bias towards high-traffic touchpoints seen in the first-touch model.</td></tr>
  <tr><td>Linear Attribution</td><td>All attribution touchpoints in completing a goal event evenly share the contribution (each gets an equal share).</td><td>Treats each touchpoint equally, some touchpoints may consistently serve as intermediary touchpoints. Evaluate if certain touchpoints with long chains can be eliminated or optimized.</td><td>Tends to favor touchpoints clicked frequently by users, amplifying their value (e.g., in search and recommendations).</td></tr>
  <tr><td> Position-Based Attribution </td><td>The first and last attribution touchpoints each receive 40% contribution, while the remaining positions evenly share the remaining 20%. </td><td>Aims to distribute value across all touchpoints but emphasizes the importance of the first and last touchpoints. Acknowledges the significance of these two touchpoints compared to others.</td><td>Subject to human bias factors.</td></tr>
</tbody>
</table>

## How to use attribution analysis
<a name="how-to-use-attribution-analysis"></a>

1.  Select an event and metric as conversion goal, you can add filter. Metric types includes:

   a. Event number: number of conversion times

   b. SumGroup: sum a value from a numerical parameter that are associated with the event selected as conversion goal

1. Select touchpoints events, you can add filter(s) to each touchpoint.

1. Click on Query to start calculation

1. You can change the time range or attribution model according to your need, which will automatically re-run the query.

1. Analysis result is displayed in a table with the following columns:

   a. Touchpoint Name: The touchpoint event name for attribution.

   b. Total Trigger Count: Number of times the touchpoint has been triggered within the specified conversion window.

   c. Number of Triggers with Conversion: Within the conversion window, number of time the touchpoint occurred simultaneously with the conversion goal.

   d. Contribution (number/sum...value): The contribution value of this touchpoint attributed to the conversion goal based on the selected model.

   e. Contribution Rate: After calculating through the attribution model, the percentage contribution of this touchpoint to the overall total. The calculation logic is the conversion goal metrics under the current attributed event divided by the sum of all conversion goals.

1. If needed, you can toggle on Associate parameter, then select parameters for both starting event and return event.

1. Repeat above step to add more metric if needed.

1. If needed, conﬁgure global ﬁlter by selecting event parameter or user attributes. Similar to event ﬁlter, you can add multiple global ﬁlters and conﬁgure the ﬁlter relationship.

1. If needed, conﬁgure grouping by selecting an event parameter or user attribute.

1. Choose Query to start the analysis.

1. Adjust the data granularity, such as Daily, Weekly, Monthly, if needed.

1. Specify query time range.

## Example
<a name="example-3"></a>

 Calculate the retention rate of new customers who downloaded from different app markets on Android one week ago.

1.  Select the **Attribution Analysis** model.

1.  Choose purchase as the conversion event, choose sumGroup by [event]value as conversion metric

1. Choose The day as conversion window.

1. Select view\_live as touchpoint event, add filter of live\_id = live\_1.

1.  Repeat step 4 to add touchpoints for the rest of three live channel.

1.  Click **Query** .

 All configurations are as shown in the image below:

![Attribution analysis interface with multiple dropdown menus and input fields for data analysis.](https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/attribution.png)
