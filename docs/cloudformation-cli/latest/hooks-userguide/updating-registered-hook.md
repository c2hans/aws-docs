---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/updating-registered-hook.html
---

# Updating a custom Hook
<a name="updating-registered-hook"></a>

Updating a custom Hook allows revisions in the Hook to be made available in the CloudFormation registry.

To update a custom Hook, submit your revisions to the CloudFormation registry through the CloudFormation CLI [https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html) operation.

```
$ cfn submit
```

To specify the default version of your Hook in your account, use the [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html) command and specify the type, type name, and version ID.

```
$ aws cloudformation set-type-default-version \
    --type HOOK \
    --type-name {{MyCompany::Testing::MyTestHook}} \
    --version-id {{00000003}}
```

To retrieve information about the versions of a Hook, use [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-type-versions.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-type-versions.html).

```
$ aws cloudformation list-type-versions \
  --type HOOK \
  --type-name "{{MyCompany::Testing::MyTestHook}}"
```
