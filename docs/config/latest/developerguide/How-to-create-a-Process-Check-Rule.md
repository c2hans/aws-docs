---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/How-to-create-a-Process-Check-Rule.html
---

# Include Process Checks Within a Conformance Pack
<a name="How-to-create-a-Process-Check-Rule"></a>

1. Add a process check in the conformance pack template. Refer to [Sample Conformance Pack Template for Creating Process Checks](Sample-CPack-Template-for-Creating-Process-Check-Rule.md).

   ```
   Resources:
     ConfigEnabledAllRegions:
       Properties:
         ConfigRuleName: Config-Enabled-All-Regions
         Description: Ensure AWS Config is enabled in all Regions.
         Source:
           Owner: AWS
           SourceIdentifier: AWS_CONFIG_PROCESS_CHECK
       Type: AWS::Config::ConfigRule
   ```

1. Enter the name for the process check.

1. Enter the description for the process check.

1. Deploy the conformance pack. For more information, see [Deploying Conformance Packs for AWS Config](conformance-pack-deploy.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
