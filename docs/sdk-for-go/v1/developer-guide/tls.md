---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/tls.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Enforcing a minimum TLS version in the AWS SDK for Go
<a name="tls"></a>

To add increased security when communicating with AWS services, you should configure your client to use TLS 1.2 or later.

**Note**
As of [Go 1.18](https://go.dev/doc/go1.18#tls10), the TLS configuration used by the `net/http#Client` defaults to TLS 1.2 as a minimum, and disables support for TLS 1.0 and TLS 1.1.

## How do I set my TLS version?
<a name="how-do-i-set-my-tls-version"></a>

You can set the TLS version to 1.2 using the following code.

1. Create a custom HTTP transport to require a minimum version of TLS 1.2

   ```
   tr := &http.Transport{
       TLSClientConfig: &tls.Config{
           MinVersion: tls.VersionTLS12,
       },
   }
   ```

1. Configure the transport.

   ```
   // In Go versions earlier than 1.13
   err := http2.ConfigureTransport(tr)
   if err != nil {
       fmt.Println("Got an error configuring HTTP transport")
       fmt.Println(err)
       return
   }

   // In Go versions later than 1.13
   tr.ForceAttemptHTTP2 = true
   ```

1. Create an HTTP client with the configured transport, and use that to create a session. REGION is the AWS Region, such as *us-west-2*.

   ```
   client := http.Client{Transport: tr}

   sess := session.Must(session.NewSession(&aws.Config{
       Region:     &REGION,
       HTTPClient: &client,
   }))
   ```

1. Use the following function to confirm your TLS version.

   ```
   func GetTLSVersion(tr *http.Transport) string {
       switch tr.TLSClientConfig.MinVersion {
       case tls.VersionTLS10:
           return "TLS 1.0"
       case tls.VersionTLS11:
           return "TLS 1.1"
       case tls.VersionTLS12:
           return "TLS 1.2"
       case tls.VersionTLS13:
           return "TLS 1.3"
       }

       return "Unknown"
   }
   ```

1. Confirm your TLS version by calling *GetTLSVersion*.

   ```
   if tr, ok := sess.Config.HTTPClient.Transport.(*http.Transport); ok {
       log.Printf("Client uses %v", GetTLSVersion(tr))
   }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
