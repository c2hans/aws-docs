---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-release-history-790.html
---

# Amazon EMR 7.9.0 - Hadoop release notes
<a name="Hadoop-release-history-790"></a>

## Amazon EMR 7.9.0 - Hadoop changes
<a name="Hadoop-release-history-790-changes"></a>

| Type | Description |
| --- | --- |
| New Feature | Automatic Configuration Mapping: EMRFS filesystem configuration are automatically applied to corresponding S3A filessystem configuration enabling seamless migration from EMRFS to S3A. |
| New Feature |  [YARN Conatainer bin-packing](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-container-yarn.html): scheduling policy for aggresive downscaling |
| Backport |  YARN-11752 : Global Scheduler: Improve the container allocation time |
| Bug Fix |  S3A: Fix IAMCredentialsProvider Returning Expired Credentials  |
| Bug Fix |  Fix `yarn.log.server.url` configuration value for clusters with in-transit encryption enabled |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
