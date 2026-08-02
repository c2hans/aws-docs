---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StandardsControlAssociationId.html
---

# StandardsControlAssociationId
<a name="API_StandardsControlAssociationId"></a>

 An array with one or more objects that includes a security control (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. The security control ID or ARN is the same across standards.

## Contents
<a name="API_StandardsControlAssociationId_Contents"></a>

 ** SecurityControlId **   <a name="securityhub-Type-StandardsControlAssociationId-SecurityControlId"></a>
 The unique identifier (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) of a security control across standards.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** StandardsArn **   <a name="securityhub-Type-StandardsControlAssociationId-StandardsArn"></a>
 The ARN of a standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_StandardsControlAssociationId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StandardsControlAssociationId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StandardsControlAssociationId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StandardsControlAssociationId)
