---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/account-pools-list.html
---

# List account pools for a domain
<a name="account-pools-list"></a>

To use the AWS CLI to view the account pools in a domain, use the `list-account-pools` command.
+ Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI to run the `list-account-pools` command with the following format, where the domain ID is a required argument.

  ```
  aws datazone list-account-pools --domain-identifier {{DOMAIN_ID}}
  ```

  Example command:

  ```
  aws datazone list-account-pools --domain-identifier {{dzd_dkqsou2EXAMPLE}}
  ```

  This command returns output with the account pool details.

  ```
  {
      "items": [
          {
              "domainId": "{{dzd_dkqsou2EXAMPLE}}",
              "id": "5htvndro7wd89z",
              "name": "my-accountpool",
              "resolutionStrategy": "MANUAL",
              "domainUnitId": "4njnngous3oyw7",
              "createdBy": "",
              "updatedBy": ""
          }
      ]
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
