---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-cloudfront.html
---

# Amazon CloudFront Utilities
<a name="sdk-utilities-cloudfront"></a>

## Amazon CloudFront URL Signer
<a name="cflong-url-signer"></a>

 The Amazon CloudFront URL signer simplifies the process of creating signed URLs. A signed URL includes information, such as an expiration date and time, that enables you to control access to your content. Signed URLs are useful when you want to distribute content through the internet, but want to restrict access to certain users (for example, to users who have paid a fee).

 To sign a URL, create a `URLSigner` instance with your CloudFront key pair ID and the associated private key. Then call the `Sign` or `SignWithPolicy` method and include the URL to sign. For more information about Amazon CloudFront key pairs, see [Creating CloudFront Key Pairs for Your Trusted Signers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html#private-content-creating-cloudfront-key-pairs) in the CloudFront Developer Guide.

 The following example creates a signed URL that's valid for one hour after it is created.

```
import "github.com/aws/aws-sdk-go-v2/feature/cloudfront/sign"

// ...

signer := sign.NewURLSigner(keyID, privKey)

signedURL, err := signer.Sign(rawURL, time.Now().Add(1*time.Hour))
if err != nil {
    log.Fatalf("Failed to sign url, err: %s\n", err.Error())
    return
}
```

 For more information about the signing utility, see the [sign](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/cloudfront/sign) package in the AWS SDK for Go API Reference.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go v2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
