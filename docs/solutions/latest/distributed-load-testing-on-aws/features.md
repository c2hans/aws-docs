---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/features.html
---

# Features
<a name="features"></a>

The solution provides the following features:

 **Multiple Test Framework Support**

Supports JMeter, k6, and Locust test scripts, as well as simple HTTP endpoint testing without requiring custom scripts. For more information, refer to [Test types](design-considerations.md#test-types) in the Architecture details section. For security considerations about the bundled frameworks, refer to [Third-party testing frameworks](security-1.md#third-party-testing-frameworks).

 **Two Traffic Shape Modes**

Controls the load either from the solution or from your script. In Standard mode, you set the virtual users, ramp-up, and hold duration, and the solution applies them to whichever framework the test uses. In Native mode, the solution runs your script under the framework’s own command line and honors the load the script declares. For more information, refer to [Traffic shape modes](design-considerations.md#traffic-shape-modes-architecture) in the Architecture details section.

 **High User Load Simulation**

Simulates tens of thousands of concurrent virtual users to stress test your application under realistic load conditions.

 **Multi-Region Load Distribution**

Distributes load tests across multiple AWS Regions to simulate geographically distributed user traffic and assess global performance.

 **Flexible Test Scheduling**

Schedules tests to run immediately, at a specific future date and time, or on a recurring schedule using cron expressions for automated regression testing.

 **Real-Time Monitoring**

Provides optional live data streaming to monitor test progress with real-time metrics including response times, virtual user counts, and request success rates.

 **Comprehensive Test Results**

Displays detailed test results with performance metrics, percentiles (p50, p90, p95, p99), error analysis, and downloadable artifacts for offline analysis.

 **Baseline Comparison**

Designates baseline test runs for performance comparison to track improvements or regressions over time.

 **Endpoint Flexibility**

Tests any HTTP or HTTPS endpoint across AWS Regions, on-premises environments, or other cloud providers.

 **Flexible Web Console Hosting**

Choose from three web console hosting options: Amazon CloudFront \+ S3 (default), ALB \+ ECS Fargate with a custom domain, or headless (bring your own web server). The ALB \+ ECS Fargate option supports environments with VPC Block Public Access policies or zero public internet exposure requirements common in regulated industries. The backend and authentication remain the same across all options. For more information, refer to [Deploy the solution](deploy-the-solution.md).

 **Intuitive Web Console**

Provides a web-based console for creating, managing, and monitoring tests with no command-line interaction required.

 **AI-Assisted Analysis (Optional)**

Integrates with AI development tools through the Model Context Protocol (MCP) server for intelligent analysis of load testing data.

 **Multiple Protocol Support**

Supports various protocols including HTTP, HTTPS, WebSocket, JDBC, JMS, FTP, and gRPC through custom test scripts.
