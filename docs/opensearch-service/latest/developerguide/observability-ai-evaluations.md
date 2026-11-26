---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-ai-evaluations.html
---

# Agent evaluations

With agent evaluations, you can measure the quality of your AI agents. You score agent runs with checks in code, with an LLM judge, or with an evaluation library. The SDK sends each score to OpenSearch next to the trace of the agent run. In OpenSearch UI, you can then compare agent versions and review test runs case by case. You can also open the trace that each result judged.

Agent evaluations is for developers who build and operate AI agents. For example, you can check that a support agent uses the data that its tools return, block a prompt change that makes a test suite fail, or have an LLM judge grade a sample of production conversations each day.

You can evaluate an agent in the following ways:

*Offline evaluation*
Run a test suite against your agent before you release a change. A test suite is a fixed set of cases, each with an input and an optional expected output. Each run of the suite has a name, such as `v2 prompt`, so you can compare it with earlier runs.

*Online evaluation*
Score the traces of production traffic after the agent runs. For example, a scheduled job reads recent agent traces from OpenSearch and judges them.

## Concepts
<a name="observability-ai-evaluations-concepts"></a>

Agent evaluations uses the following terms.

Evaluation result
One verdict on one agent span, trace, or session. A result has a score, a label such as `pass` or `fail`, and an explanation. Each result is an OpenTelemetry log event named `gen_ai.evaluation.result`. The event carries the trace ID and span ID of the agent run that it judged.

Evaluation and evaluator
An evaluation is what you measure, for example `plan_quality`. The evaluator is what produced the result: a check in code (`code`), an LLM judge (`llm_judge`), or a person (`human`). For an LLM judge, the result also records the judge model, the judge prompt name and version, and the trace of the judge call.

Pass rule
A threshold and a direction, such as a score of at least 4, or a `pass` or `fail` label. A result without a pass rule shows its score only.

Test suite, run, and case
A test suite is a set of cases. A run executes every case of the suite against one agent version. The run records one result for each case and evaluation. A case passes when all of its results pass.

Agent and version
Results are grouped by the agent name and version of the agent run that they judged (`gen_ai.agent.name` and `gen_ai.agent.version`). This grouping lets you compare two versions of the same agent.

## How agent evaluations works
<a name="observability-ai-evaluations-how"></a>

Your evaluation code uses the OpenSearch GenAI SDK to score agent runs. The SDK sends traces, agent logs, and evaluation results over OTLP to an OpenSearch Ingestion pipeline, which writes them to three indexes:
+ Spans go to `otel-v1-apm-span*` (`otel-v2-apm-span*` for an observability stack on a domain with the engine optimized for log analytics).
+ Log events named `gen_ai.evaluation.result` go to `otel-v1-genai-evaluation*`.
+ Agent logs go to `logs-otel-v1*`.

The Evaluations pages in OpenSearch UI read the evaluation index and the span index, and open the trace behind each result in Agent Traces. For a diagram of this flow, see [Architecture](observability-ai.md#observability-ai-architecture).

## Data model and ingestion
<a name="observability-ai-evaluations-data-model"></a>

Each evaluation result is a `gen_ai.evaluation.result` event, as defined in the OpenTelemetry [semantic conventions for generative AI events](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-events.md#event-gen_aievaluationresult), and is one document in the evaluation index. The event definition covers the evaluation name, score, label, and explanation. The Evaluations pages also use the agent, version, and test suite fields in the following list, which the event definition doesn't include. The Evaluations pages use the following fields:
+ `traceId` and `spanId` – The agent run that the result judged. For a session result, `gen_ai.conversation.id` instead.
+ `gen_ai.evaluation.name`, `gen_ai.evaluation.score.value`, `gen_ai.evaluation.score.label`, and `gen_ai.evaluation.explanation` – What was measured, the score, the verdict, and why.
+ `gen_ai.agent.name` and `gen_ai.agent.version` – The agent version that the result belongs to.
+ `test.suite.name`, `test.suite.run.id`, and `test.case.id` – For offline results, the test suite, run, and case.

The evaluation index uses a dedicated index template, which maps the fields that the Evaluations pages filter and group on as keywords. The index setup depends on the storage backend.

OpenSearch Service domain
A write alias, `otel-v1-genai-evaluation`, points to rolling indexes named `otel-v1-genai-evaluation-000001`, `-000002`, and so on. An Index State Management (ISM) policy rolls the index over at 50 GB or after 24 hours. Create the ISM policy, the index template, and the first index before the pipeline first writes. OpenSearch Ingestion can't create ISM policies or aliases.

OpenSearch Serverless collection
One index, `otel-v1-genai-evaluation`. The pipeline creates it on first write from the template in its configuration. The index has no ISM policy and doesn't roll over. Retention comes from the collection's data lifecycle policy.

An observability stack sets up the evaluation index for you. Its pipeline has the evaluation route and template, and on a managed domain it creates the ISM policy, the template, and the write alias. For information about setting up the index yourself, see [Data model and ingestion](https://observability.opensearch.org/docs/agent-evals/data-model/) in the OpenSearch observability stack documentation.

## Getting started with agent evaluations
<a name="observability-ai-evaluations-getting-started"></a>

This procedure sends your first evaluation results to OpenSearch and shows them in OpenSearch UI. Use it after you instrument your agent for tracing, as described in [Getting started](observability-ai.md#observability-ai-getting-started). The procedure takes about 15 minutes.

Before you begin, make sure that you have the following:
+ An OpenSearch Ingestion pipeline with the evaluation route and index described in [How agent evaluations works](#observability-ai-evaluations-how).
+ An IAM identity with `osis:Ingest` permission on the pipeline.
+ An OpenSearch UI workspace whose data source holds the traces and the evaluation results.

**To send evaluation results and view them**

1. Install the Python SDK 0.3.0 or later.

   ```bash
   pip install "opensearch-genai-observability-sdk-py>=0.3.0"
   ```

   For TypeScript, install the TypeScript SDK 0.2.0 or later instead.

   ```bash
   npm install "@opensearch-project/genai-observability-sdk-ts@>=0.2.0"
   ```

1. Register the SDK with your pipeline's traces and logs endpoints and with SigV4 signing.

   The following Python code example registers the SDK. Evaluation results travel as logs, so set both endpoints. Replace the placeholder values with your own.

   ```python
   # Requires opensearch-genai-observability-sdk-py 0.3.0 or later
   from opensearch_genai_observability_sdk_py import register

   register(
       service_name="travel-assistant",
       agent_name="travel_assistant",
       traces_endpoint="https://{{pipeline-endpoint}}/{{traces-path}}",
       logs_endpoint="https://{{pipeline-endpoint}}/{{logs-path}}",
       sigv4={"service": "osis", "region": "{{region}}"},
   )
   ```

   The example uses the following values:
   + `service_name` – The name of your application in the traces.
   + `agent_name` – The name that the Evaluations pages group results under.
   + {{pipeline-endpoint}} – The ingestion endpoint of your OpenSearch Ingestion pipeline.
   + {{traces-path}} and {{logs-path}} – The OTLP traces and logs paths configured in your pipeline.
   + {{region}} – The AWS Region of your pipeline, such as `aa-example-1`.

1. Run a test suite offline with `evaluate()`.

   In the following Python code example, each case's agent run is its own trace, and each scorer's result links to that trace. `evaluate()` records a failed agent run or scorer as an error result and continues with the next case.

   ```python
   from opensearch_genai_observability_sdk_py import evaluate, scorer

   @scorer(name="uses_tool_data", evaluator_type="code")
   def uses_tool_data(input, output, expected) -> bool:
       return "sunny" in output.lower()

   result = evaluate(
       name="travel-assistant-suite",
       task=run_agent,  # your agent, instrumented with @observe
       data=[{"case_id": "tc-paris", "input": "Plan a one-day trip to Paris.",
              "expected": "Mentions the sunny weather and one event."}],
       scores=[uses_tool_data],
       agent_version="v2",
       run_name="v2 prompt",
   )
   ```

1. Score production traffic online with `score()`.

   In the following Python code example, `root` is the root span of a recent agent trace that you read with `OpenSearchTraceRetriever`. The example records the verdict on that span and logs a failure instead of stopping the job.

   ```python
   import logging
   from opensearch_genai_observability_sdk_py import score

   logger = logging.getLogger(__name__)

   try:
       score(
           "plan_quality", 5,
           trace_id=root.trace_id, span_id=root.span_id,
           agent_name=root.agent_name, agent_version=root.agent_version,
           threshold=4, score_min=1, score_max=5,
           evaluator="travel_plan_judge", evaluator_type="llm_judge",
           explanation="Uses the weather and events from the tools.",
       )
       logger.info("Recorded plan_quality for trace %s", root.trace_id)
   except Exception as err:
       logger.error("Could not record plan_quality for trace %s: %s", root.trace_id, err)
   ```

1. In OpenSearch UI, open your observability workspace. In the left navigation, under **Agent Monitoring**, choose **Evaluations**. Set the time range to include the time of your runs.

When you finish, the **Agents** tab lists your agent version with its pass rate, and the **Eval runs** tab lists the `v2 prompt` run. The procedure creates no AWS resources to clean up. The evaluation results stay in the evaluation index under its retention settings.

For complete runnable examples, including LLM judges, evaluation libraries such as DeepEval and RAGAS, and a GitHub Action that gates pull requests on evaluation results, see the [agent evaluations quickstart](https://observability.opensearch.org/docs/agent-evals/quickstart/) and [agent evaluations in CI](https://observability.opensearch.org/docs/agent-evals/ci/) in the OpenSearch observability stack documentation.

## Evaluations UI
<a name="observability-ai-evaluations-ui"></a>

The Evaluations pages have three tabs: **Agents**, **Eval runs**, and **Eval results**. The time range applies to all of them. On each tab, choose **All**, **Online**, or **Offline** to limit the results to one source.

### Agents
<a name="observability-ai-evaluations-agents"></a>

The **Agents** tab lists one row for each agent version that has evaluation results in the time range. Each row shows the pass rate, the number of results, and the time of the last result.

Choose a row to open the agent. The agent page has three tabs:
+ **Overview** – Shows the pass rate over time for each version. It also compares two versions evaluation by evaluation, sorted by the change between them.
+ **Test suites** – Lists the agent's offline runs.
+ **Results** – Lists the agent's individual results.

The following screenshot shows the **Overview** tab for the Travel Planner agent over 7 days. It has two parts: a line chart of the pass rate of each version over time, and a table that compares the pass rate of each evaluation between the versions.

The chart shows the following:
+ Version 1.3.0 has results for all 7 days. Its pass rate stays between about 75% and 97%.
+ Version 1.4.0 has results for the last 4 days only, after it started taking traffic alongside 1.3.0. Its pass rate stays between about 85% and 100%, with one drop to about 65%.

The table compares 672 results for 1.3.0 with 140 results for 1.4.0, as follows:
+ **Response time** – 78% for 1.3.0 and 94% for 1.4.0, 16 points more.
+ **No repeated tool calls** – 88% for 1.3.0 and 98% for 1.4.0, 10 points more.
+ **Tool call success** – 90% for 1.3.0 and 96% for 1.4.0, 6 points more.
+ **Stays on destination** – 95% for 1.3.0 and 96% for 1.4.0, 1 point more.
+ **Task completion** – 92% for 1.3.0 and 84% for 1.4.0, 8 points less.

![Overview tab of the Travel Planner agent, with a two-line chart and a five-row comparison table.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/agent-evals/eval-agent-detail.png)

### Eval runs
<a name="observability-ai-evaluations-runs"></a>

The **Eval runs** tab lists offline runs, newest first. Each row shows the test suite, the agent version, the cases passed, and the pass rate.

Choose a run to open its page. The page shows the following:
+ The cases passed, the results passed, and the evaluator errors, each compared with the run before.
+ What each evaluation checks.
+ The run's cases. Expand a case to see its input, output, expected output, and each result with its explanation. Choose **View trace** to open the case's agent trace.

The following image shows the page of the `v2 prompt` run. The run passed 4 of 5 cases and 14 of 15 results, 3 more than the run before. The failed case, `paris_day_trip`, is expanded. It failed `answer_length` and passed the other two evaluations.

![A test run summary with one case expanded to show its input, outputs, and results.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/agent-evals/eval-case.png)

Choose a result to open its details. For an LLM judge, the details show what the evaluation checks, the judge model, the judge prompt, the explanation, and the input and output that the judge saw. Choose **View judge trace** to open the trace of the judge call.

The following image shows the details of a `plan_quality` result. The judge model scored the answer 5 out of 5 with the `travel-plan-quality@v1` prompt.

![Details of an LLM judge result, with the score, judge model, judge prompt, and explanation.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/agent-evals/eval-result-flyout.png)

To compare two runs of the same test suite and agent, select them on the **Eval runs** tab and choose **Compare 2 runs**. You can also choose **Compare with run before** on a run page. The comparison lists the cases that regressed or were fixed, and the pass rate of each evaluation in both runs.

On the comparison, choose a case to compare the traces of the two runs for that case. The **Timeline** tab shows both traces on one time scale and highlights the spans that appear in only one trace. The **Trace map** tab shows the same difference as a graph of agent and tool calls.

The following image compares the traces of the Berlin case, which has no travel dates, between the 1.3.0 release run (run A) and the 1.4.0 candidate run (run B). Run B skips the weather agent, so its plan has no forecast and the case regressed. The traces differ as follows:
+ Both traces start with the Travel Planner agent span and a planning LLM call of about 1.6 seconds.
+ Run A then calls the weather agent, which calls its forecast tool. The weather agent spans appear only in run A and are highlighted. Run B goes straight to the events agent.
+ Run A takes 5.4 seconds and has 58 spans. Run B takes 4.3 seconds and has 41 spans.
+ The output of run A includes the Berlin weather. The output of run B has no forecast, which is why the case regressed in run B.

![Timelines of one test case from two runs, with the weather agent spans shown only in run A.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/agent-evals/eval-compare.png)

### Eval results
<a name="observability-ai-evaluations-results"></a>

The **Eval results** tab lists every result, online and offline, newest first. Each row shows the agent, version, evaluation, verdict, score, and explanation. Filter by agent, evaluation, version, or verdict, and choose a row to open the result. Choose the target to open the span, trace, or session that the result judged.

### Evaluations settings
<a name="observability-ai-evaluations-settings"></a>

Agent evaluations reads two datasets in the workspace:
+ A traces dataset over the agent spans. The default is `otel-v1-apm-span*`.
+ An evaluations dataset over the evaluation results. The default is `otel-v1-genai-evaluation*`, with the time field `@timestamp`.

To change the datasets, choose **Settings** on the Evaluations page. An observability stack creates both datasets.
