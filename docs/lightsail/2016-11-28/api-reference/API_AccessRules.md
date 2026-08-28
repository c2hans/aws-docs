---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AccessRules.html
---

# AccessRules
<a name="API_AccessRules"></a>

Describes the anonymous access permissions for an Amazon Lightsail bucket and its objects.

For more information about bucket access permissions, see [Understanding bucket permissions in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-understanding-bucket-permissions) in the

 *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_AccessRules_Contents"></a>

 ** allowPublicOverrides **   <a name="Lightsail-Type-AccessRules-allowPublicOverrides"></a>
A Boolean value that indicates whether the access control list (ACL) permissions that are applied to individual objects override the `getObject` option that is currently specified.
When this is true, you can use the [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) Amazon S3 API action to set individual objects to public (read-only) using the `public-read` ACL, or to private using the `private` ACL.
Type: Boolean
Required: No

 ** getObject **   <a name="Lightsail-Type-AccessRules-getObject"></a>
Specifies the anonymous access to all objects in a bucket.
The following options can be specified:
+  `public` - Sets all objects in the bucket to public (read-only), making them readable by anyone in the world.

  If the `getObject` value is set to `public`, then all objects in the bucket default to public regardless of the `allowPublicOverrides` value.
+  `private` - Sets all objects in the bucket to private, making them readable only by you or anyone you give access to.

  If the `getObject` value is set to `private`, and the `allowPublicOverrides` value is set to `true`, then all objects in the bucket default to private unless they are configured with a `public-read` ACL. Individual objects with a `public-read` ACL are readable by anyone in the world.
Type: String
Valid Values: `public | private`
Required: No

## See Also
<a name="API_AccessRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AccessRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AccessRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AccessRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
