---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_anonymous.html
---

# Create anonymous clients in the SDK for PHP
<a name="guide_credentials_anonymous"></a>

In some cases, you might want to create a client that is not associated with any credentials. This enables you to make anonymous requests to a service.

For example, you can configure both Amazon S3 objects and Amazon CloudSearch domains to allow anonymous access.

To create an anonymous client, you set the `'credentials'` option to `false`.

```
$s3Client = new S3Client([
    'version'     => 'latest',
    'region'      => 'us-west-2',
    'credentials' => false
]);

// Makes an anonymous request. The object would need to be publicly
// readable for this to succeed.
$result = $s3Client->getObject([
    'Bucket' => 'amzn-s3-demo-bucket',
    'Key'    => 'my-key',
]);
```
