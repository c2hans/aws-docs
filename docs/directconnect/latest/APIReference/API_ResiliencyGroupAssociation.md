---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ResiliencyGroupAssociation.html
---

# ResiliencyGroupAssociation
<a name="API_ResiliencyGroupAssociation"></a>

Information about an association between a connection and a resiliency group.

## Contents
<a name="API_ResiliencyGroupAssociation_Contents"></a>

 ** connectionArn **   <a name="DX-Type-ResiliencyGroupAssociation-connectionArn"></a>
The Amazon Resource Name (ARN) of the associated connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** resiliencyGroupId **   <a name="DX-Type-ResiliencyGroupAssociation-resiliencyGroupId"></a>
The ID of the resiliency group.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `^(dxrg|DXRG)-[0-9a-zA-Z]{17}$`
Required: No

 ** state **   <a name="DX-Type-ResiliencyGroupAssociation-state"></a>
The state of the association. The valid values are `associating`, `associated`, `disassociating`, and `disassociated`.
Type: String
Valid Values: `associating | associated | disassociating | disassociated`
Required: No

## See Also
<a name="API_ResiliencyGroupAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/ResiliencyGroupAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/ResiliencyGroupAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/ResiliencyGroupAssociation)
