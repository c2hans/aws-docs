---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchAttachTypedLink.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchAttachTypedLink
<a name="API_BatchAttachTypedLink"></a>

Attaches a typed link to a specified source and target object inside a [BatchRead](API_BatchRead.md) operation. For more information, see [AttachTypedLink](API_AttachTypedLink.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchAttachTypedLink_Contents"></a>

 ** Attributes **   <a name="amazoncds-Type-BatchAttachTypedLink-Attributes"></a>
A set of attributes that are associated with the typed link.
Type: Array of [AttributeNameAndValue](API_AttributeNameAndValue.md) objects
Required: Yes

 ** SourceObjectReference **   <a name="amazoncds-Type-BatchAttachTypedLink-SourceObjectReference"></a>
Identifies the source object that the typed link will attach to.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** TargetObjectReference **   <a name="amazoncds-Type-BatchAttachTypedLink-TargetObjectReference"></a>
Identifies the target object that the typed link will attach to.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** TypedLinkFacet **   <a name="amazoncds-Type-BatchAttachTypedLink-TypedLinkFacet"></a>
Identifies the typed link facet that is associated with the typed link.
Type: [TypedLinkSchemaAndFacetName](API_TypedLinkSchemaAndFacetName.md) object
Required: Yes

## See Also
<a name="API_BatchAttachTypedLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAttachTypedLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAttachTypedLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAttachTypedLink)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
