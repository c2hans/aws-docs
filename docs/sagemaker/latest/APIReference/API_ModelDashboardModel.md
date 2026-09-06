---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDashboardModel.html
---

# ModelDashboardModel
<a name="API_ModelDashboardModel"></a>

A model displayed in the Amazon SageMaker Model Dashboard.

## Contents
<a name="API_ModelDashboardModel_Contents"></a>

 ** Endpoints **   <a name="sagemaker-Type-ModelDashboardModel-Endpoints"></a>
The endpoints that host a model.
Type: Array of [ModelDashboardEndpoint](API_ModelDashboardEndpoint.md) objects
Required: No

 ** LastBatchTransformJob **   <a name="sagemaker-Type-ModelDashboardModel-LastBatchTransformJob"></a>
A batch transform job. For information about SageMaker batch transform, see [Use Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html).
Type: [TransformJob](API_TransformJob.md) object
Required: No

 ** Model **   <a name="sagemaker-Type-ModelDashboardModel-Model"></a>
A model displayed in the Model Dashboard.
Type: [Model](API_Model.md) object
Required: No

 ** ModelCard **   <a name="sagemaker-Type-ModelDashboardModel-ModelCard"></a>
The model card for a model.
Type: [ModelDashboardModelCard](API_ModelDashboardModelCard.md) object
Required: No

 ** MonitoringSchedules **   <a name="sagemaker-Type-ModelDashboardModel-MonitoringSchedules"></a>
The monitoring schedules for a model.
Type: Array of [ModelDashboardMonitoringSchedule](API_ModelDashboardMonitoringSchedule.md) objects
Required: No

## See Also
<a name="API_ModelDashboardModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelDashboardModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelDashboardModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelDashboardModel)
