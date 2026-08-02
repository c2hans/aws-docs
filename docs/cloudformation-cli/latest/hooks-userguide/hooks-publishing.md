---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-publishing.html
---

# Publishing Hooks for public use
<a name="hooks-publishing"></a>

To develop a public third-party Hook, develop your Hook as a private extension. Then, in each AWS Region in which you want to make the extension publicly available:

1. Register your Hook as a private extension in the CloudFormation registry.

1. Test your Hook to make sure it meets all necessary requirements for being published in the CloudFormation registry.

1. Publish your Hook to the CloudFormation registry.
**Note**
Before you publish any extension in a given Region, you must first register as an extension publisher in that Region. To do this in multiple Regions simultaneously, see [Publishing extensions in multiple Regions using StackSets](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension-stacksets.html) in the * CloudFormation CLI User Guide*.

After you've developed and registered your Hook, you can make it publicly available to general CloudFormation users by *publishing* it to the CloudFormation registry, as a third-party public extension.

Public third-party Hooks enable you to offer CloudFormation users to proactively inspect the configuration of AWS resources before provisioning. As with private Hooks, public Hooks are treated the same as any Hook published by AWS within CloudFormation.

Hooks published to the registry are visible by all CloudFormation users in the AWS Regions in which they're published. Users can then *activate* your extension in their account, which makes it available for use in their templates. For more information, see [Use third-party public extensions from the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html) in the *CloudFormation User Guide*.

For more information, see [Publishing extensions to make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html) in the * CloudFormation CLI User Guide*.
