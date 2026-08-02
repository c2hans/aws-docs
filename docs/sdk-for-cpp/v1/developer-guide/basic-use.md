---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/basic-use.html
---

# Initializing and shutting down the AWS SDK for C\+\+
<a name="basic-use"></a>

Applications that use the AWS SDK for C\+\+ must initialize it. Similarly, before the application terminates, the SDK must be shut down. Both operations accept configuration options that affect the initialization and shutdown processes and subsequent calls to the SDK.

All applications that use the AWS SDK for C\+\+ must include the file `aws/core/Aws.h`.

The AWS SDK for C\+\+ must be initialized by calling `Aws::InitAPI`. Before the application terminates, the SDK must be shut down by calling `Aws::ShutdownAPI`. Each method accepts an argument of [https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-core/html/struct_aws_1_1_s_d_k_options.html](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-core/html/struct_aws_1_1_s_d_k_options.html). All other calls to the SDK can be performed between these two method calls.

**All AWS SDK for C\+\+ calls performed between `Aws::InitAPI` and `Aws::ShutdownAPI` should either to be contained within a pair of curly braces or should be invoked by functions called between the two methods.**

A basic skeleton application is shown below.

```
#include <aws/core/Aws.h>
int main(int argc, char** argv)
{
   Aws::SDKOptions options;
   Aws::InitAPI(options);
   {
      {{// make your SDK calls here.}}
   }
   Aws::ShutdownAPI(options);
   return 0;
}
```

**The SDK for C\+\+ and its dependencies use C\+\+ static objects, and the order of static object destruction is not determined by the C\+\+ standard. To avoid memory issues caused by the nondeterministic order of static variable destruction, do not wrap the calls to `Aws::InitAPI` and `Aws::ShutdownAPI` into another static object. **
