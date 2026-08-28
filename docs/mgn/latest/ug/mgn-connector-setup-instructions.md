---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-setup-instructions.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Set up the MGN Connector
<a name="mgn-connector-setup-instructions"></a>

In order to set up your MGN connector, take the following steps:

1. Make sure your account has the required permissions as defined in [MGN connector permissions](mgn-connector-permissions.md).

1. If the MGN connector manages source servers from multiple accounts, set up the global view feature and set up your AWS Organization, following the instructions [here](global-view.md).

   After you set up your AWS Organization, configure the CloudFormation StackSet to create the required role per management account. Use the template "Enable AWS Transform MGN Connector access". Full instructions are available [here](setting-up-stacksets.md).

1.  If the MGN connector manages source servers from a single account, and both the MGN connector and the source servers belong to the same account:

   1.  After replacing the example account number **111122223333** with your account number, create a role using the following trust policy:

------
#### [ JSON ]

****

      ```
      {
          "Version":"2012-10-17",
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "AWS": "arn:aws:iam::{{111122223333}}:role/AWSApplicationMigrationConnectorManagementRole"
                  },
                  "Action": "sts:AssumeRole"
              }
          ]
      }
      ```

------

   1.  Attach the **AWSApplicationMigrationAgentInstallationPolicy** policy to the Permission policies.

   1.  Name the role **AWSApplicationMigrationConnectorSharingRole\_ACCOUNT-ID** (replace **ACCOUNT-ID** with your account number).

1.  [Create a new MGN connector](add-connector.md) on the MGN connectors page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
