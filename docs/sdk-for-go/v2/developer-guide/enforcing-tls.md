---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/enforcing-tls.html
---

# Enforcing a minimum TLS version
<a name="enforcing-tls"></a>

 To add increased security when communicating with AWS services, you must configure your client to use TLS 1.2 or later. To work with AWS services, the underlying Go runtime must support a minimum version of TLS 1.2, but TLS 1.3 is recommended.

 TLS 1.3 is the prerequisite to enable post-quantum cryptography, which might require additional actions or configurations. For more information, see [Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html) in the AWS SDKs and Tools Reference Guide.

**Note**
 As of [Go 1.18](https://go.dev/doc/go1.18#tls10) on the Go website, the TLS configuration used by `net/http` defaults to a minimum of TLS 1.2 and disables support for TLS 1.0 and TLS 1.1.

## Setting the TLS version
<a name="how-do-i-set-my-tls-version"></a>

 In the AWS SDK for Go v2, you configure the minimum TLS version by providing a custom HTTP client whose transport specifies a [tls.Config](https://pkg.go.dev/crypto/tls#Config), which is documented on the Go package documentation website. For more information about customizing the HTTP client, see [Customize the HTTP Client](configure-http.md).

 The following example builds an HTTP client that requires a minimum of TLS 1.2 and passes it to `config.LoadDefaultConfig`.

```
import (
    "context"
    "crypto/tls"
    "log"
    "net/http"

    awshttp "github.com/aws/aws-sdk-go-v2/aws/transport/http"
    "github.com/aws/aws-sdk-go-v2/config"
)

// ...

httpClient := awshttp.NewBuildableClient().WithTransportOptions(func(tr *http.Transport) {
    tr.TLSClientConfig = &tls.Config{
        MinVersion: tls.VersionTLS12,
    }
})

cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithHTTPClient(httpClient))
if err != nil {
    log.Fatalf("failed to load configuration, %v", err)
}
```

 To require TLS 1.3, set `MinVersion` to `tls.VersionTLS13`.

**Note**
 Some AWS services do not yet support TLS 1.3. Setting TLS 1.3 as your minimum version might affect interoperability. We recommend testing this change with each service before deploying to production.
