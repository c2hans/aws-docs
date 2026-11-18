---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent.html
---

# Apache Spark Troubleshooting Agent for Amazon EMR and AWS Glue
<a name="spark-troubleshooting-agent"></a>

The Apache Spark Troubleshooting Agent for Amazon EMR is a conversational AI capability that simplifies the troubleshooting of Apache Spark applications on Amazon EMR (EMR on EC2, EMR Serverless, and EMR on EKS), AWS Glue, and Amazon SageMaker notebooks. Traditional Spark troubleshooting requires extensive manual analysis of logs, performance metrics, and error patterns to identify root causes and code fixes. The Troubleshooting Agent simplifies this process through natural language prompts, automated workload analysis, and intelligent code recommendations.

You can use the Troubleshooting Agent to troubleshoot PySpark and Scala application failures. The agent analyzes your failed jobs, identifies performance bottlenecks, and provides actionable recommendations and code fixes, while giving you full control over implementation decisions.

When you ask about a failed run, the `analyze_spark_workload` tool uses the Troubleshooting Agent. For setup, pricing, and architecture, see [Spark Troubleshooting and Optimization Agents](spark-troubleshoot.md).

## How the Troubleshooting Agent works
<a name="spark-troubleshooting-agent-how"></a>

To start the troubleshooting process, you need the identifiers of your failed Spark applications running on a supported platform (EMR on EC2, EMR Serverless, EMR on EKS, AWS Glue, or Amazon SageMaker notebooks). The application must have accessible logs, Spark History Server data, and configuration details, and you must have permission to read the platform resources and application metadata. You then submit a prompt such as the following to start the workflow:

```
Analyze my EMR step execution failure, EMR id {{step-id}} with cluster id {{cluster-id}}
```

The agent orchestrates the troubleshooting by using specialized tools. The workflow follows these steps:

1. **Feature extraction and context building** – The agent collects and analyzes telemetry data from your Spark application, including Spark History Server logs, configuration settings, and error traces. It extracts key performance metrics, resource utilization patterns, and failure signatures to build a context profile for the analysis.

1. **Analysis and root cause identification** – The agent uses AI models and a Spark knowledge base to correlate the extracted features and identify the root cause of the failure or performance issue. You receive the following:
   + **Analysis insights** – Technical details about what the agent discovered and analyzed.
   + **Root cause** – A clear explanation of what went wrong and why.
   + **Initial assessment** – Whether the issue is code-related, configuration-related, or resource-related, with general guidance for mitigation.

1. **Code recommendations (when applicable)** – If the analysis identifies a code-related issue based on the error classification, the agent can use the code recommendation tool to provide a specific fix, with exact before-and-after code and suggested replacements.

The troubleshooting process is iterative. You can continue the conversation to dive deeper into a specific issue, and you can use the tools interactively during local Spark code development to fix bugs or improve your code. Test recommended changes in a non-production run before you apply them to production jobs.

**Topics**
+ [How the Troubleshooting Agent works](#spark-troubleshooting-agent-how)
+ [Using the Troubleshooting Agent](spark-troubleshooting-using-troubleshooting-agent.md)
+ [Troubleshooting features and capabilities](spark-troubleshooting-features.md)
+ [Troubleshooting prompt examples](spark-troubleshooting-agent-prompt-examples.md)
