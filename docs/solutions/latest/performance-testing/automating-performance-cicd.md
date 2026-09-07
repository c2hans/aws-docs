---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/automating-performance-cicd.html
---

# Automating Performance in CI/CD
<a name="automating-performance-cicd"></a>

Performance testing delivers the most value when it runs automatically on every change, not as a manual gate before major releases. The "Test After Every Change" principle requires pipeline integration that makes performance results as visible as unit test results.

## Where Performance Tests Fit in the Pipeline
<a name="where-performance-tests-fit"></a>

![Where Performance Tests Fit in the Pipeline](https://docs.aws.amazon.com/solutions/latest/performance-testing/images/perf_cicd_pipeline.png)

## Integration Approach: Tool Agnostic
<a name="integration-approach"></a>

DLT provides multiple integration points that work with any CI/CD system:

| Integration Method | How It Works | Best For |
| --- | --- | --- |
| DLT REST API | Start tests and poll results via HTTP calls | Any CI/CD tool with HTTP support |
| DLT CLI | Command-line interface with IAM/Cognito auth | Pipeline scripts, headless environments |
| Scheduled Tests | Cron-based recurring tests configured in DLT | Nightly regression suites |
| MCP Server | AI-assisted analysis of test results | Developer productivity workflows |

## Pipeline Integration Pattern
<a name="pipeline-integration-pattern"></a>

The general pattern for any CI/CD tool:

1. **Trigger:** Pipeline stage invokes DLT CLI or API to start a pre-defined test scenario

1. **Wait:** Poll for test completion (DLT CLI supports waiting with timeout)

1. **Evaluate:** Compare results against the designated baseline run

1. **Gate:** If p99 latency or error rate exceeds threshold, fail the pipeline

1. **Report:** Publish results as pipeline artifacts for team review

## Concrete Example: GitHub Actions with DLT CLI
<a name="concrete-example-github-actions"></a>

This workflow runs a performance gate on every push to `main`. It starts a DLT scenario, waits for completion, and fails the build if p99 exceeds the baseline by more than 15%.

```
# .github/workflows/perf-gate.yml
name: Performance Gate
on:
  push:
    branches: [main]

jobs:
  load-test:
    runs-on: ubuntu-latest
    permissions:
      id-token: write    # For OIDC auth to AWS
      contents: read
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::111122223333:role/dlt-ci-role
          aws-region: us-east-1

      - name: Install DLT CLI
        run: pip install distributed-load-testing-cli

      - name: Run load test
        run: |
          dlt run \
            --test-id "regression-suite" \
            --wait \
            --timeout 1200 \
            --output results.json

      - name: Evaluate results against baseline
        run: |
          # Extract p99 from results and compare to baseline
          P99=$(jq '.results.avg_lt_p99' results.json)
          BASELINE_P99=$(jq '.baseline.avg_lt_p99' results.json)
          THRESHOLD=$(echo "$BASELINE_P99 * 1.15" | bc)
          if (( $(echo "$P99 > $THRESHOLD" | bc -l) )); then
            echo "::error::Performance regression detected. p99=${P99}ms exceeds baseline+15%=${THRESHOLD}ms"
            exit 1
          fi
          echo "Performance gate PASSED. p99=${P99}ms within threshold=${THRESHOLD}ms"

      - name: Upload results artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: dlt-results
          path: results.json
```

Adapt the same pattern for GitLab CI (use `script:` blocks), Jenkins (use `sh` steps in a Declarative Pipeline), or AWS CodePipeline (invoke DLT via a Lambda action or CodeBuild step).

## Baseline Management
<a name="baseline-management"></a>

DLT supports designating any test run as a "baseline" for comparison. Establish your baseline strategy:
+ Run a baseline test on every stable release (tag it in DLT)
+ Compare every subsequent test against this baseline
+ Update the baseline only when performance improvements are intentional
+ Track baseline drift over time to detect gradual degradation

## Scheduling Recurring Tests
<a name="scheduling-recurring-tests"></a>

For the "Always Test" principle, configure DLT scheduled tests:

| Test Cadence | Purpose | Typical Configuration |
| --- | --- | --- |
| Nightly | Catch regressions from daily merges | Full load test, moderate concurrency |
| Weekly | Endurance validation | 4-8 hour soak test at 60% expected peak |
| Pre-event | Validate capacity for planned spikes | Spike test at 150% expected peak |
| Monthly | Stress testing to find new ceilings | Ramp to failure |

## Handling Performance Test Failures in the Pipeline
<a name="handling-performance-test-failures"></a>

When a performance test fails your gate criteria, the team needs a clear escalation path. Without one, teams either ignore the failure ("just override it") or block releases indefinitely.

| Failure Severity | Response | Example |
| --- | --- | --- |
| Minor (p99 regressed 10-20%) | Investigate, create performance ticket, allow deploy with team lead approval | New logging added 15ms to p99 |
| Moderate (p99 regressed 20-50%) | Block deploy, investigate same day, fix or revert within 24 hours | N\+1 query introduced in new feature |
| Critical (p99 regressed >50% or errors >5%) | Revert immediately, root cause analysis before re-deploy | Connection pool misconfiguration |

Automate severity classification in your pipeline. Compare the regression percentage against thresholds and route notifications appropriately: minor failures go to a Slack channel, moderate failures page the team lead, critical failures trigger an automatic revert.

## Dealing with Flaky Performance Tests
<a name="dealing-with-flaky-performance-tests"></a>

Performance tests have inherent variance. A 2% latency difference between runs is noise, not signal. Reduce false positives with these techniques:
+ **Run multiple iterations.** Execute the same test 3 times and use the median result for gate decisions. DLT scheduled tests support this pattern.
+ **Use statistical significance thresholds.** A 5% regression that falls within normal variance (based on historical run data) should not fail the pipeline.
+ **Warm up the environment.** Run a 30-second warm-up phase before the measured phase. Exclude warm-up metrics from gate evaluation.
+ **Isolate test infrastructure.** Shared staging environments produce inconsistent results. Dedicated performance test environments with consistent instance types eliminate infrastructure variance.
+ **Monitor the test infrastructure itself.** If your Fargate tasks are CPU-constrained, results reflect the test harness limit, not the application's actual capacity.

## Put It Into Practice
<a name="put-it-into-practice-cicd"></a>
+ Identify which CI/CD tool your team uses
+ Deploy the DLT CLI in your pipeline agent/runner (IAM auth recommended for automation)
+ Create a "smoke" performance test: 50 VUs, 2 minutes, run on every PR merge
+ Create a "full" performance test: production-scale VUs, 15 minutes, run nightly
+ Set up pipeline failure criteria: fail if p99 > baseline \+ 15% or error rate > 1%

**Go Deeper**
[DLT CLI Documentation](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/dlt-cli.html)
[Performance Efficiency Pillar: Process and Culture](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/process-and-culture.html) (Well-Architected)
