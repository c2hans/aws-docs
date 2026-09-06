---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/testing.html
---

# Testing
<a name="testing"></a>

## Functional tests
<a name="functional-tests"></a>

This solution includes a set of functional tests against the deployed solution to verify the basic operations of this solution. Users can run these tests by using the following steps:

1. Deploy this solution. If you have previously deployed this solution, skip this step.

1. Clone the [solution’s repository](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/tree/main).

1. Open a new terminal session and navigate to the `source/tests/functional_tests` directory.

1. Run the following command. Replace the ` <stack-name> ` and ` <profile-name> ` variables with name of the stack deployed in step 1 and profile name of AWS CLI credentials, respectively. Replace the ` <in-venv-flag> ` with 1 if the tests are running in an existing Python virtual environment or with 0 if not. See the [README.md](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/blob/main/source/tests/functional_tests/README.md) file of functional tests on the GitHub repository for further details.

   ```
   $ sh run-functional-tests.sh [-h] [-v] [--test-file-name] [--extras] [--region] --stack-name <stack-name> --profile <profile-name> --in-venv <in-venv-flag>
   ```

## Distributed Load Testing (DLT)
<a name="distributed-load-testing-dlt"></a>

The load testing tools based on [JMeter](https://jmeter.apache.org/) and [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) are an optional part of the solution, and can be used to verify basic operations and the configuration installed can scale to the capacity required for successful operation.

Two JMeter test plans are included with the solution source code and can be used standalone with JMeter or used for large-scale, multi-Region load testing with Distributed Load Testing on AWS.

### Prebid Server test plan
<a name="prebid-server-test-plan"></a>

This test plan is placed in `source/loadtest/jmx/prebid_server_test_plan.jmx`. It uses several commercial bidding adapters in Prebid Server configured to respond in test mode. The bidding adapters do not make connections over the Internet when invoked this way and respond with fixed data. This test plan is suitable for verifying basic operations of the deployed stack are working.

To use this test plan, follow these steps:

1. Deploy this solution. If you have previously deployed this solution, skip this step.

1. Open the test plan `source/loadtest/jmx/prebid_server_test_plan.jmx` in JMeter.

1. Update the URL under **User Defined Variables** in JMeter console with the CloudFront endpoint of Prebid Server deployed in step 1.

1. Install the [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) solution.

1. Open the **Distributed Load Testing on AWS** console.

1. Upload the updated test plan in step 3 and start the tests.
