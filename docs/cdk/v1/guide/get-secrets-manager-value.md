---
source_url: https://docs.aws.amazon.com/cdk/v1/guide/get-secrets-manager-value.html
---

This is the AWS CDK v1 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and will now only receive critical bug fixes and security patches. New features will be developed for CDK v2 exclusively. Support for CDK v1 will end entirely on June 1, 2023. [Migrate to CDK v2](work-with-cdk-v2.md) to have access to the latest features and fixes.

# Get a value from AWS Secrets Manager
<a name="get-secrets-manager-value"></a>

To use values from AWS Secrets Manager in your AWS CDK app, use the [fromSecretAttributes()](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.Secret.html#static-fromwbrsecretwbrattributesscope-id-attrs) method. It represents a value that is retrieved from Secrets Manager and used at CloudFormation deployment time.

------
#### [ TypeScript ]

```
import * as sm from "@aws-cdk/aws-secretsmanager";

export class SecretsManagerStack extends core.Stack {
  constructor(scope: core.App, id: string, props?: core.StackProps) {
    super(scope, id, props);

    const secret = sm.Secret.fromSecretAttributes(this, "ImportedSecret", {
      secretCompleteArn:
        "arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name>-<random-6-characters>"
      // If the secret is encrypted using a KMS-hosted CMK, either import or reference that key:
      // encryptionKey: ...
    });
```

------
#### [ JavaScript ]

```
const sm = require("@aws-cdk/aws-secretsmanager");

class SecretsManagerStack extends core.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    const secret = sm.Secret.fromSecretAttributes(this, "ImportedSecret", {
      secretCompleteArn:
        "arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name>-<random-6-characters>"
      // If the secret is encrypted using a KMS-hosted CMK, either import or reference that key:
      // encryptionKey: ...
    });
  }
}

module.exports = { SecretsManagerStack }
```

------
#### [ Python ]

```
import aws_cdk.aws_secretsmanager as sm

class SecretsManagerStack(core.Stack):
    def __init__(self, scope: core.App, id: str, **kwargs):
      super().__init__(scope, name, **kwargs)

      secret = sm.Secret.from_secret_attributes(self, "ImportedSecret",
          secret_complete_arn="arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name>-<random-6-characters>",
          # If the secret is encrypted using a KMS-hosted CMK, either import or reference that key:
          # encryption_key=....
      )
```

------
#### [ Java ]

```
import software.amazon.awscdk.services.secretsmanager.Secret;
import software.amazon.awscdk.services.secretsmanager.SecretAttributes;

public class SecretsManagerStack extends Stack {
    public SecretsManagerStack(App scope, String id) {
        this(scope, id, null);
    }

    public SecretsManagerStack(App scope, String id, StackProps props) {
        super(scope, id, props);

        Secret secret = (Secret)Secret.fromSecretAttributes(this, "ImportedSecret", SecretAttributes.builder()
            .secretCompleteArn("arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name>-<random-6-characters>")
             // If the secret is encrypted using a KMS-hosted CMK, either import or reference that key:
             // .encryptionKey(...)
             .build());
    }
}
```

------
#### [ C\# ]

```
using Amazon.CDK.AWS.SecretsManager;

public class SecretsManagerStack : Stack
{
    public SecretsManagerStack(App scope, string id, StackProps props) : base(scope, id, props) {

        var secret = Secret.FromSecretAttributes(this, "ImportedSecret", new SecretAttributes {
            SecretCompleteArn = "arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name>-<random-6-characters>"
            // If the secret is encrypted using a KMS-hosted CMK, either import or reference that key:
            // encryptionKey = ...,
        });
    }
```

------

**Tip**
Use the [create-secret](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.Secret.html) CLI command to create a secret from the command-line, such as when testing:

```
aws secretsmanager create-secret --name ImportedSecret --secret-string mygroovybucket
```
The command returns an ARN you can use with the above example.

Once you have created a `Secret` instance, you can get the secret's value from the instance's `secretValue` attribute. The value is represented by a `[SecretValue](https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_core.SecretValue.html)` instance, a special type of [Tokens](tokens.md). As it is a token, it has meaning only after resolution; your CDK app does not need to access its actual value, but can instead pass the `SecretValue` instance (or its string or numeric representation) to whatever CDK method needs the value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
