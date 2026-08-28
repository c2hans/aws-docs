---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-DetectAnomalies.html
---

# DetectAnomalies
<a name="dqdl-rule-types-DetectAnomalies"></a>

 Detects anomalies for a given data quality rule. Every execution of DetectAnomalies rule result in saving evaluated value for the given rule. When there is enough data gathered, anomaly detection algorithm takes all historical data for that given rule and runs anomaly detection. DetectAnomalies rule fails when anomaly is detected. More info about what anomaly was detected can be obtained from Observations.

**Syntax**

```
       DetectAnomalies {{<RULE_NAME>}} {{<RULE_PARAMETERS>}}
```

 `RULE_NAME` – The name of the rule that you want to evaluate and detect anomalies for. Supported rules:
+ "RowCount"
+ "Completeness"
+ "Uniqueness"
+ "Mean"
+ "Sum"
+ "StandardDeviation"
+ "Entropy"
+ "DistinctValuesCount"
+ "UniqueValueRatio"
+ "ColumnLength"
+ "ColumnValues"
+ "ColumnCorrelation"
+ "CustomSQL"
+ "ColumnCount"

 `RULE_PARAMETERS` – some rules require additional parameters to run. Refer to the given rule documentation to see required parameters.

**Example: Anomalies for RowCount**

For example, if we want to detect RowCount anomalies, we provide RowCount as a rule name.

```
DetectAnomalies "RowCount"
```

**Example: Anomalies for ColumnLength**

For example, if we want to detect ColumnLength anomalies, we provide ColumnLength as a rule name and the column name.

```
DetectAnomalies "ColumnLength" "id"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
