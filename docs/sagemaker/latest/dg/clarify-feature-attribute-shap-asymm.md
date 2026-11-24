---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-shap-asymm.html
---

# Asymmetric Shapley Values

**Note**
Amazon SageMaker Clarify is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Clarify, but we do not plan to introduce new features. For more information, see [Clarify availability change](clarify-availability-change.md).

The SageMaker Clarify time series forecasting model explanation solution is a feature attribution method rooted in [cooperative game theory](https://en.wikipedia.org/wiki/Cooperative_game_theory), similar in spirit to SHAP. Specifically, Clarify uses [random order group values](http://www.library.fa.ru/files/Roth2.pdf#page=121), also known as [asymmetric Shapley values](https://proceedings.neurips.cc/paper/2020/file/0d770c496aa3da6d2c3f2bd19e7b9d6b-Paper.pdf) in machine learning and explainability.

## Background
<a name="clarify-feature-attribute-shap-asymm-setting"></a>

The goal is to compute attributions for input features to a given forecasting model *f*. The forecasting model takes the following inputs:
+ Past time series *(target TS)*. For example, this could be past daily train passengers in the Paris-Berlin route, denoted by *x<sub>t</sub>​*.
+ (Optional) A covariate time series. For example, this could be festivities and weather data, denoted by *z<sub>t</sub>* ​∈ R<sup>S</sup>. When used, covariate TS could be available only for the past time steps or also for the future ones (included in the festivity calendar).
+ (Optional) Static covariates, such as quality of service (like 1st or 2nd class), denoted by *u* ∈ R<sup>E</sup>.

Static covariates, dynamic covariates, or both can be omitted, depending on the specific application scenario. Given a prediction horizon K ≥ 0 (e.g. K=30 days) the model prediction can be characterized by the formula: *f(x<sub>[1:T]</sub>, z<sub>[1:T\+K]</sub>, u) = x<sub>[T\+1:T \+K\+1]</sub>*.

The following diagram shows a dependency structure for a typical forecasting model. The prediction at time *t\+1* depends on the three types of inputs previously mentioned.

![Dependency structure for a typical forecasting model.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/clarify/clarify-forecast-dependency.png)

## Method
<a name="clarify-feature-attribute-shap-asymm-explan"></a>

Explanations are computed by querying the time series model *f* on a series of points derived by the original input. Following game theoretic constructions, Clarify averages differences in predictions led by obfuscating (that is, setting to a baseline value) parts of the inputs iteratively. The temporal structure can be navigated in a chronological or anti-chronological order or both. Chronological explanations are built by iteratively adding information from the first time step, while anti-chronological from the last step. The latter mode may be more appropriate in the presence of recency bias, such as when forecasting stock prices. One important property of the computed explanations is that they sum to the original model output if the model provides deterministic outputs.

## Resulting attributions
<a name="clarify-feature-attribute-shap-asymm-attr"></a>

Resulting attributions are scores that mark individual contributions of specific time steps or input features toward the final forecast at each forecasted time step. Clarify offers the following two granularities for explanations:
+ Timewise explanations are inexpensive and provide information about specific time steps only, such as how much the information of the 19th day in the past contributed to the forecasting of the 1st day in the future. These attributions do not explain individually static covariates and aggregate explanations of target and covariate time series. The attributions are a matrix *A* where each *A<sub>tk</sub>​* is the attribution of time step *t* toward forecasting of time step *T\+k*. Note that if the model accepts future covariates, *t* can be greater than *T*.
+ Fine-grained explanations are more computationally intensive and provide a full breakdown of all attributions of the input variables.
**Note**
Fine-grained explanations only support chronological order.

  The resulting attributions are a triplet composed of the following:
  + Matrix *A<sup>x</sup>* ∈ R<sup>T×K</sup> related to the input time series, where *A<sub>tk</sub><sup>x​</sup>* is the attribution of *x<sub>t</sub>* toward forecasting step *T\+k*
  + Tensor *A<sup>z</sup>* ∈ *R<sup>T\+K×S×K</sup>* related to the covariate time series, where *A<sub>tsk</sub><sup>z​</sup>* is the attribution of *z<sub>ts​</sub>* (i.e. the sth covariate TS) toward forecasting step *T\+k*
  + Matrix *A<sup>u</sup>* ∈ R<sup>E×K</sup> related to the static covariates, where *A<sub>ek</sub><sup>u</sup>​* is the attribution of *u<sub>e</sub>* ​(the eth static covariate) toward forecasting step *T\+k*

Regardless of the granularity, the explanation also contains an offset vector *B* ∈ *R<sup>K</sup>* that represents the “basic behavior” of the model when all data is obfuscated.
