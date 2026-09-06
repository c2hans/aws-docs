---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-operations-planning/splits-leakage.html
---

# Splits and data leakage
<a name="splits-leakage"></a>

Data leakage happens when your model gets data during inference—the moment the model is in production and receiving prediction requests—that it shouldn't have access to, such as data samples that were used for training, or information that will not be available when the model is deployed in production.

If your model is inadvertently tested on training data, data leakage might cause overfitting. Overfitting means that your model doesn't generalize well to unseen data. This section provides best practices to avoid data leakage and overfitting.

## Split your data into at least three sets
<a name="split-your-data-into-at-least-three-sets"></a>

One common source of data leakage is dividing (splitting) your data improperly during training. For example, the data scientist might have knowingly or unknowingly trained the model on the data that was used for testing. In such situations, you might observe very high success metrics that are caused by overfitting. To solve this issue, you should split the data into at least three sets: training, validation, and testing.

By splitting your data in this way, you can use the validation set to choose and tune the parameters you use to control the learning process (*hyperparameters*).  When you have achieved a desired result or reached a plateau of improvement, perform evaluation on the testing set. The performance metrics for the testing set should be similar to the metrics for the other sets. This indicates there is no distribution mismatch between the sets, and your model is expected to generalize well in production.

## Use a stratified split algorithm
<a name="stratified-algorithm"></a>

When you split your data into training, validation, and testing for small datasets, or when you work with highly imbalanced data, make sure to use a stratified split algorithm. Stratification guarantees that each split contains approximately the same number or distribution of classes for each split. The [scikit-learn ML library](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) already implements stratification, and so does [Apache Spark](https://spark.apache.org/docs/3.5.3/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.sampleBy.html).

For sample size, make sure that the validation and testing sets have enough data for evaluation, so you can reach statistically significant conclusions. For example, a common split size for relatively small datasets (fewer than 1 million samples) is 70%, 15%, and 15%, for training, validation, and testing. For very large datasets (more than 1 million samples), you might use 90%, 5%, and 5%, to maximize the available training data.

In some use cases, it's useful to split the data into additional sets, because the production data might have experienced radical, sudden changes in distribution during the period in which it was being collected. For example, consider a data collection process for building a demand forecasting model for grocery store items. If the data science team collected the training data during 2019 and the testing data from January 2020 through March 2020, a model would probably score well on the testing set. However, when the model is deployed in production, the consumer pattern for certain items would have already changed significantly because of the COVID-19 pandemic, and the model would generate poor results. In this scenario, it would make sense to add another set (for example, recent\_testing`)` as an additional safeguard for model approval. This addition could prevent you from approving a model for production that would instantly perform poorly because of distribution mismatch.

In some instances, you might want to create additional validation or testing sets that include specific types of samples, such as data associated with minority populations. These data samples are important to get right but might not be well represented in the overall dataset. These data subsets are called *slices*.

Consider the case of an ML model for credit analysis that was trained on data for an entire country, and was balanced to equally account for the entire domain of the target variable. Additionally, consider that this model might have a City feature. If the bank that uses this model expands its business into a specific city, it might be interested in how the model performs for that region. So, an approval pipeline should not only assess the model's quality based on the test data for the entire country, but should evaluate test data for a given city slice as well.

When data scientists work on a new model, they can easily assess the model's capabilities and account for edge cases by integrating under-represented slices in the validation stage of the model.

## Consider duplicate samples when doing random splits
<a name="duplicates"></a>

Another, less common, source of leakage is in datasets that might contain too many duplicate samples. In this case, even if you split the data into subsets, different subsets might have samples in common. Depending on the number of duplicates, overfitting might be mistaken for generalization.

## Consider features that might not be available when receiving inferences in production
<a name="consider-features-that-might-not-be-available-when-receiving-inferences-in-production"></a>

Data leakage also happens when models are trained with features that are not available in production, at the instant the inferences are invoked. Because models are often built based on historical data, this data might be enriched with additional columns or values that were not present at some point in time. Consider the case of a credit approval model that has a feature that tracks how many loans a customer has made with the bank in the past six months. There is a risk of data leakage if this model is deployed and used for credit approval for a new customer who doesn't have a six-month history with the bank.

[Amazon SageMaker Feature Store](https://aws.amazon.com/sagemaker/feature-store/) helps solve this problem. You can test your models more accurately with the use of time travel queries, which you can use to view data at specific points in time.
