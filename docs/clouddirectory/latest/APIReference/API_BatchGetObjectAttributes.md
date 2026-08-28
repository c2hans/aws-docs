---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchGetObjectAttributes.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchGetObjectAttributes
<a name="API_BatchGetObjectAttributes"></a>

Retrieves attributes within a facet that are associated with an object inside an [BatchRead](API_BatchRead.md) operation. For more information, see [GetObjectAttributes](API_GetObjectAttributes.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchGetObjectAttributes_Contents"></a>

 ** AttributeNames **   <a name="amazoncds-Type-BatchGetObjectAttributes-AttributeNames"></a>
List of attribute names whose values will be retrieved.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 230.
Pattern: `^[a-zA-Z0-9._:-]*$`
Required: Yes

 ** ObjectReference **   <a name="amazoncds-Type-BatchGetObjectAttributes-ObjectReference"></a>
Reference that identifies the object whose attributes will be retrieved.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** SchemaFacet **   <a name="amazoncds-Type-BatchGetObjectAttributes-SchemaFacet"></a>
Identifier for the facet whose attributes will be retrieved. See [SchemaFacet](API_SchemaFacet.md) for details.
Type: [SchemaFacet](API_SchemaFacet.md) object
Required: Yes

## See Also
<a name="API_BatchGetObjectAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchGetObjectAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchGetObjectAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchGetObjectAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
