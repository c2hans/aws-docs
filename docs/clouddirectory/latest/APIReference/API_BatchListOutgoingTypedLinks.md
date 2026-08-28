---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchListOutgoingTypedLinks.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchListOutgoingTypedLinks
<a name="API_BatchListOutgoingTypedLinks"></a>

Returns a paginated list of all the outgoing [TypedLinkSpecifier](API_TypedLinkSpecifier.md) information for an object inside a [BatchRead](API_BatchRead.md) operation. For more information, see [ListOutgoingTypedLinks](API_ListOutgoingTypedLinks.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchListOutgoingTypedLinks_Contents"></a>

 ** ObjectReference **   <a name="amazoncds-Type-BatchListOutgoingTypedLinks-ObjectReference"></a>
The reference that identifies the object whose attributes will be listed.
Type: [ObjectReference](API_ObjectReference.md) object
Required: Yes

 ** FilterAttributeRanges **   <a name="amazoncds-Type-BatchListOutgoingTypedLinks-FilterAttributeRanges"></a>
Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
Type: Array of [TypedLinkAttributeRange](API_TypedLinkAttributeRange.md) objects
Required: No

 ** FilterTypedLink **   <a name="amazoncds-Type-BatchListOutgoingTypedLinks-FilterTypedLink"></a>
Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.
Type: [TypedLinkSchemaAndFacetName](API_TypedLinkSchemaAndFacetName.md) object
Required: No

 ** MaxResults **   <a name="amazoncds-Type-BatchListOutgoingTypedLinks-MaxResults"></a>
The maximum number of results to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NextToken **   <a name="amazoncds-Type-BatchListOutgoingTypedLinks-NextToken"></a>
The pagination token.
Type: String
Required: No

## See Also
<a name="API_BatchListOutgoingTypedLinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
