---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# Intrinsic function reference
<a name="intrinsic-function-reference"></a>

CloudFormation provides several built-in functions that help you manage your stacks. Use intrinsic functions in your templates to assign values to properties that are not available until runtime.

**Note**
You can use intrinsic functions only in specific parts of a template. Currently, you can use intrinsic functions in resource properties, outputs, metadata attributes, and update policy attributes. You can also use intrinsic functions to conditionally create stack resources.

**Topics**
+ [`Fn::Base64`](intrinsic-function-reference-base64.md)
+ [`Fn::Cidr`](intrinsic-function-reference-cidr.md)
+ [Condition functions](intrinsic-function-reference-conditions.md)
+ [`Fn::FindInMap`](intrinsic-function-reference-findinmap.md)
+ [`Fn::ForEach`](intrinsic-function-reference-foreach.md)
+ [`Fn::GetAtt`](intrinsic-function-reference-getatt.md)
+ [`Fn::GetAZs`](intrinsic-function-reference-getavailabilityzones.md)
+ [`Fn::GetStackOutput`](intrinsic-function-reference-getstackoutput.md)
+ [`Fn::ImportValue`](intrinsic-function-reference-importvalue.md)
+ [`Fn::Join`](intrinsic-function-reference-join.md)
+ [`Fn::Length`](intrinsic-function-reference-length.md)
+ [`Fn::Select`](intrinsic-function-reference-select.md)
+ [`Fn::Split`](intrinsic-function-reference-split.md)
+ [`Fn::Sub`](intrinsic-function-reference-sub.md)
+ [`Fn::ToJsonString`](intrinsic-function-reference-ToJsonString.md)
+ [`Fn::Transform`](intrinsic-function-reference-transform.md)
+ [`Ref`](intrinsic-function-reference-ref.md)
+ [Rule functions](intrinsic-function-reference-rules.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
