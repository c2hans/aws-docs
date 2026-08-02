---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsTeamMember.html
---

# AwsTeamMember
<a name="API_AwsTeamMember"></a>

Represents an AWS team member for the engagement. This structure includes details such as name, email, and business title.

## Contents
<a name="API_AwsTeamMember_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BusinessTitle **   <a name="AWSPartnerCentral-Type-AwsTeamMember-BusinessTitle"></a>
Specifies the AWS team member's business title and indicates their organizational role.
Type: String
Valid Values: `AWSSalesRep | AWSAccountOwner | WWPSPDM | PDM | PSM | ISVSM`
Required: No

 ** Email **   <a name="AWSPartnerCentral-Type-AwsTeamMember-Email"></a>
Provides the AWS team member's email address.
Type: String
Pattern: `(?=.{0,80}$)[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?`
Required: No

 ** FirstName **   <a name="AWSPartnerCentral-Type-AwsTeamMember-FirstName"></a>
Provides the AWS team member's first name.
Type: String
Pattern: `(?s).{0,80}`
Required: No

 ** LastName **   <a name="AWSPartnerCentral-Type-AwsTeamMember-LastName"></a>
Provides the AWS team member's last name.
Type: String
Pattern: `(?s).{0,80}`
Required: No

## See Also
<a name="API_AwsTeamMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsTeamMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsTeamMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsTeamMember)
