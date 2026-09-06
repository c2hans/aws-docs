---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Grantee.html
---

# Grantee
<a name="API_Grantee"></a>

Container for the person being granted permissions.

## Contents
<a name="API_Grantee_Contents"></a>

 ** Type **   <a name="AmazonS3-Type-Grantee-Type"></a>
Type of grantee
Type: String
Valid Values: `CanonicalUser | AmazonCustomerByEmail | Group`
Required: Yes

 ** DisplayName **   <a name="AmazonS3-Type-Grantee-DisplayName"></a>

Type: String
Required: No

 ** EmailAddress **   <a name="AmazonS3-Type-Grantee-EmailAddress"></a>

Type: String
Required: No

 ** ID **   <a name="AmazonS3-Type-Grantee-ID"></a>
The canonical user ID of the grantee.
Type: String
Required: No

 ** URI **   <a name="AmazonS3-Type-Grantee-URI"></a>
URI of the grantee group.
Type: String
Required: No

## See Also
<a name="API_Grantee_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Grantee)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Grantee)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Grantee)
