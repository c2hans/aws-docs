---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/test.html
---

# Testing
<a name="test"></a>

When you replatform a COBOL application while maintaining Db2 for z/OS as the shared database, it's crucial to ensure that the new system functions equivalently to the original. This hybrid environment presents unique challenges and opportunities for testing. The following strategy outlines a comprehensive approach to functional equivalence testing and is designed to validate the replatformed application's performance, data integrity, and seamless integration with the existing Db2 for z/OS database.

Start by identifying the critical business processes and transactions that need to be compared between systems. Then, create a detailed test plan with specific scenarios that will effectively evaluate the functional equivalence of these transactions. Finally, develop comprehensive test data sets that cover all identified scenarios, and make sure that they are identical for both systems to enable accurate comparison.

## Source environment
<a name="source-env"></a>
+ Initial snapshot (first snapshot):
  + Make sure that the data table isn't being used by other applications during the test, because this can affect the equivalence test.
  + Take a snapshot of the Db2 for z/OS tables that are used by the transaction before running any tests.
+ Source system testing:
  + Run the full suite of tests on the original COBOL application.
  + Record all transactions, inputs, and outputs.
  + Monitor system performance and resource utilization.
+ Post-source testing snapshot (second snapshot):
  + Take another snapshot of the Db2 for z/OS database after you complete the source system tests.

## Target environment
<a name="target-env"></a>
+ Database reset:
  + Restore the database to its initial state by using the first snapshot.
+ Target system testing (replatformed environment):
  + Run the same suite of tests on the replatformed application.
  + Make sure that all target system tests use the same inputs as the source system tests.
  + Monitor system performance and resource utilization.
+ Post-target testing snapshot (third snapshot):
  + Take a final snapshot of the Db2 for z/OS database after you complete the target system tests.

## Analysis
<a name="analysis"></a>
+ Comparison and analysis:
  + Compare the second and third snapshots to identify any discrepancies in data.
  + Analyze test results, and compare the outputs from the source and target systems.
  + Evaluate performance metrics between the two environments.
+ Integration testing:
  + Perform tests that involve both the replatformed application and any remaining COBOL components.
  + Verify seamless interaction between the two environments.
+ Failover and recovery testing:
  + Test scenarios where one environment fails and the other environment takes over.
  + Ensure data consistency and integrity during failover situations.
+ Load and stress testing:
  + Conduct tests with varying loads to assess how the hybrid system performs under stress.
  + Identify any bottlenecks or performance issues in either environment.
+ Documentation and reporting:
  + Document all test results, discrepancies, and performance metrics.
  + Prepare a comprehensive report that compares the source and target systems.

## Testing your application in AWS Mainframe Modernization
<a name="m2-application-testing"></a>

The [AWS Mainframe Modernization Application Testing](https://aws.amazon.com/mainframe-modernization/capabilities/testing/) service automates the execution of application tests at scale. AWS Application Testing helps optimize and reduce mainframe application modernization and testing project costs.

**Note**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

The following diagram shows how AWS Application Testing works at a high level.

![Testing mainframe migrations with AWS Mainframe Modernization.](http://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/images/guide-img/b5c7b078-cfe6-46c4-b120-94b5824d3c88/images/df92e945-43c1-47dd-9262-20e842df96fc.png)

The process consists of these steps:

1. Create and manage test cases, which are the smallest unit of testing actions. Identify the data types that best represent functional equivalence between the source and target systems.

1. Define the configuration of the test environment by specifying CloudFormation templates and additional attributes.

1. Create test suites, which are collections of test cases.

1. Upload and replay data sets: Capture the input and output data sets on the mainframe, upload them to AWS, and then replay the test scenario on the target system.

1. Compare source and target data sets. AWS Application Testing automatically compares the output data sets from the source and target systems. Review and evaluate these to identify discrepancies.

For more information, see the [AWS Mainframe Modernization](https://docs.aws.amazon.com/m2/latest/userguide/apptest.html) documentation.
