---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/parallel-test-splitting.html
---

# About test splitting
<a name="parallel-test-splitting"></a>

AWS CodeBuild's test splitting feature allows you to parallelize your test suite execution across multiple compute instances, reducing the overall test run time. This feature is enabled through the batch configuration in your CodeBuild project settings and the `codebuild-tests-run` utility in your buildspec file.

The tests are split based on the sharding strategy specified. CodeBuild provides two sharding strategies as specified below:

Equal-distribution
The `equal-distribution` sharding strategy divides the tests across parallel builds based on the alphabetical order of the test file names. This approach first sorts the test files and then employs a chunk-based method to distribute them, ensuring that similar files are grouped together for testing. It is recommended when dealing with a relatively small set of test files. While this method aims to allocate an approximately equal number of files to each shard, with a maximum difference of one, it does not guarantee stability. When test files are added or removed in subsequent builds, the distribution of existing files may change, potentially causing reassignment across shards.

Stability
The `stability` sharding strategy employs a consistent hashing algorithm to split tests among shards, ensuring that file distribution remains stable. When new files are added or removed, this approach ensures that the existing file-to-shard assignments remain largely unchanged. For large test suites, it is recommended to use the stability option to evenly distribute the tests across shards. This mechanism aims to provide a near-equal distribution, ensuring that each shard receives a similar number of files, with only minimal variance. While the stability strategy does not guarantee an ideal equal distribution, it offers a near-equal distribution that maintains consistency in file assignments across builds, even as files are added or removed.

To enable test splitting, you need to configure the batch section in your CodeBuild project settings, specifying the desired `parallelism` level and other relevant parameters. Additionally, you'll need to include the `codebuild-tests-run` utility in your buildspec file, along with the appropriate test commands and splitting method.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
