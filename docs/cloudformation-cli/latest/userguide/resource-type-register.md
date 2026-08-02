---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-register.html
---

# Registering extensions for use in the CloudFormation registry
<a name="resource-type-register"></a>

Once you've completed developing your extension, you'll need to *register* it with CloudFormation to make it available for use in the CloudFormation registry. From the CloudFormation CLI, use the `submit` command to register your extension with CloudFormation. You can also register your resource directly using the [register-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/register-type.html) operation.

For detailed information about registering private extensions, see [Using private extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-private.html) in the *AWS CloudFormation User Guide*.

## Registering extensions using the `submit` command
<a name="resource-type-register-submit"></a>

In general, the `submit` command does the following:
+ Validates the extension schema.
+ Packages up the extension project files and uploads them to CloudFormation.
  + This includes any source code, such as resource handlers for resource type extensions.
  + Extension source code, such as resource handlers runs within the CloudFormation service account.
+ Runs the unit and contract tests defined in the extension project.
+ For resource type extensions, determines which handlers have been specified for the resource, to determine how CloudFormation provisions the resource.
+ Returns a *registration token* that you can use with the [describe-type-registration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type-registration.html) operation to track the status of the registration request.

To validate and package your extension project, but not register it with CloudFormation, use the `--dry-run` option for the `submit` command.

You must register your extension in each AWS Region in which you want to use it.

Use the [list-types](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html) operation for summary information about types that have been registered with CloudFormation, and the [describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html) operation for detailed information about specific registered resource type or resource type version.

### To enable activated Hooks
<a name="hooks-enable-activated-hooks"></a>

After you've registered and enabled your Hook, you must set the `TargetStacks` to `ALL` in the `HookConfiguration` section. For example, the following command uses the `set-type-configuration` operation and lists the `TargetStacks` as `ALL`. You may specify the `FailureMode` as `FAIL` or `WARN` and add additional properties.

```
$ aws cloudformation --region us-west-2 set-type-configuration \
  --configuration '{"CloudFormationConfiguration":{"HookConfiguration": {"TargetStacks":"ALL", "FailureMode": "FAIL", "Properties":{}}}}' \
  --type-arn ${{HOOK_TYPE_ARN}}
```

## Resource type provisioning
<a name="resource-type-register-provision-type"></a>

During registration, CloudFormation examines which resource handlers have been implemented for the resource. The handlers implemented determine what provisioning actions CloudFormation takes with respect to the resource during various stack operations.
+ If the resource type doesn't contain `create`, `read`, and `delete` handlers, CloudFormation can't actually provision the resource.
+ If the resource type doesn't contain an `update` handler, CloudFormation can't update the resource during stack update operations, and will instead replace it.

## Extension versions and scope
<a name="resource-type-register-versions"></a>

When you register an extension, you are actually registering a specific *version* of that extension. You can register multiple versions of an extension, and specify which version you want to use. Use the [SetTypeDefaultVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeDefaultVersion.html) action to specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.

Any extension you register is only visible and usable within the account(s) in which you register it.

## Deregistering extensions and extension versions
<a name="resource-type-register-deregister"></a>

To remove an extension or extension version from active use in CloudFormation, you must *deregister* it using the [DeregisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html) action. If an extension or extension version is deregistered, it can no longer be used in CloudFormation operations.

You can deregister a specific extension version, or the extension as a whole. To deregister an extension, you must individually deregister all registered versions of that extension. If an extension has only a single registered version, deregistering that version results in the extension itself being deregistered. You can't deregister the default version of an extension, unless it's the only registered version of that extension, in which case the extension itself is deregistered as well.

You can't deregister an extension using the CloudFormation console.
