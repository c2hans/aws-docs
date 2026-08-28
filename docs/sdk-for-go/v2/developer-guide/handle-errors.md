---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/handle-errors.html
---

# Handling Errors in the AWS SDK for Go V2
<a name="handle-errors"></a>

 The AWS SDK for Go returns errors that satisfy the Go `error` interface type. You can use the `Error()` method to get a formatted string of the SDK error message without any special handling. Errors returned by the SDK may implement an `Unwrap` method. The `Unwrap` method is used by the SDK to provide additional contextual information to errors, while providing access to the underlying error or chain of errors. The `Unwrap` method should be used with the [errors.As](https://golang.org/pkg/errors#As) to handle unwrapping error chains.

 It is important that your application check whether an error occurred after invoking a function or method that can return an `error` interface type. The most basic form of error handling looks similar to the following example:

```
if err != nil {
    // Handle error
    return
}
```

## Logging Errors
<a name="logging-errors"></a>

 The simplest form of error handling is traditionally to log or print the error message before returning or exiting from the application.

```
import "log"

// ...

if err != nil {
    log.Printf("error: %s", err.Error())
    return
}
```

## Service Client Errors
<a name="service-client-errors"></a>

 The SDK wraps all errors returned by service clients with the [smithy.OperationError](https://pkg.go.dev/github.com/aws/smithy-go#OperationError) error type. `OperationError` provides contextual information about the service name and operation that is associated with an underlying error. This information can be useful for applications that perform batches of operations to one or more services, with a centralized error handling mechanism. Your application can use `errors.As` to access this `OperationError` metadata.

```
import "log"
import "github.com/aws/smithy-go"

// ...

if err != nil {
    var oe *smithy.OperationError
    if errors.As(err, &oe) {
        log.Printf("failed to call service: %s, operation: %s, error: %v", oe.Service(), oe.Operation(), oe.Unwrap())
    }
    return
}
```

### API Error Responses
<a name="api-error-responses"></a>

 Service operations can return modeled error types to indicate specific errors. These modeled types can be used with `errors.As` to unwrap and determine if the operation failure was due to a specific error. For example, Amazon S3 `CreateBucket` can return a [BucketAlreadyExists](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3/types#BucketAlreadyExists) error if a bucket of the same name already exists.

 For example, to check if an error was a `BucketAlreadyExists` error:

```
import "log"
import "github.com/aws/aws-sdk-go-v2/service/s3/types"

// ...

if err != nil {
    var bne *types.BucketAlreadyExists
    if errors.As(err, &bne) {
        log.Println("error:", bne)
    }
    return
}
```

 All service API response errors implement the [smithy.APIError](https://pkg.go.dev/github.com/aws/smithy-go/#APIError) interface type. This interface can be used to handle both modeled or un-modeled service error responses. This type provides access to the error code and message returned by the service. Additionally, this type provides indication of whether the fault of the error was due to the client or server if known.

```
import "log"
import "github.com/aws/smithy-go"

// ...

if err != nil {
    var ae smithy.APIError
    if errors.As(err, &ae) {
        log.Printf("code: %s, message: %s, fault: %s", ae.ErrorCode(), ae.ErrorMessage(), ae.ErrorFault().String())
    }
    return
}
```

## Retrieving Request Identifiers
<a name="retrieving-request-identifiers"></a>

 When working with AWS Support, you may be asked to provide the request identifier that identifies the request you are attempting to troubleshoot. You can use [http.ResponseError](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/aws/transport/http#ResponseError) and use the `ServiceRequestID()` method to retrieve the request identifier associated with error response.

```
import "log"
import awshttp "github.com/aws/aws-sdk-go-v2/aws/transport/http"

// ...

if err != nil {
    var re *awshttp.ResponseError
    if errors.As(err, &re) {
        log.Printf("requestID: %s, error: %v", re.ServiceRequestID(), re.Unwrap());
    }
    return
}
```

### Amazon S3 Request Identifiers
<a name="s3-request-identifiers"></a>

 Amazon S3 requests contain additional identifiers that can be used to assist AWS Support with troubleshooting your request. You can use [s3.ResponseError](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/s3#ResponseError) and call `ServiceRequestID()` and `ServiceHostID()` to retrieve the request ID and host ID.

```
import "log"
import "github.com/aws/aws-sdk-go-v2/service/s3"

// ...

if err != nil {
    var re s3.ResponseError
    if errors.As(err, &re) {
        log.Printf("requestID: %s, hostID: %s request failure", re.ServiceRequestID(), re.ServiceHostID());
    }
    return
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go v2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
