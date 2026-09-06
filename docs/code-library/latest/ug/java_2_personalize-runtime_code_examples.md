---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/java_2_personalize-runtime_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Personalize Runtime examples using SDK for Java 2.x
<a name="java_2_personalize-runtime_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Java 2.x with Amazon Personalize Runtime.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `GetPersonalizedRanking`
<a name="personalize-runtime_GetPersonalizedRanking_java_2_topic"></a>

The following code example shows how to use `GetPersonalizedRanking`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/personalize#code-examples).

```
    public static List<PredictedItem> getRankedRecs(PersonalizeRuntimeClient personalizeRuntimeClient,
            String campaignArn,
            String userId,
            ArrayList<String> items) {

        try {
            GetPersonalizedRankingRequest rankingRecommendationsRequest = GetPersonalizedRankingRequest.builder()
                    .campaignArn(campaignArn)
                    .userId(userId)
                    .inputList(items)
                    .build();

            GetPersonalizedRankingResponse recommendationsResponse = personalizeRuntimeClient
                    .getPersonalizedRanking(rankingRecommendationsRequest);
            List<PredictedItem> rankedItems = recommendationsResponse.personalizedRanking();
            int rank = 1;
            for (PredictedItem item : rankedItems) {
                System.out.println("Item ranked at position " + rank + " details");
                System.out.println("Item Id is : " + item.itemId());
                System.out.println("Item score is : " + item.score());
                System.out.println("---------------------------------------------");
                rank++;
            }
            return rankedItems;
        } catch (PersonalizeRuntimeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return null;
    }
```
+  For API details, see [GetPersonalizedRanking](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-runtime-2018-05-22/GetPersonalizedRanking) in *AWS SDK for Java 2.x API Reference*.

### `GetRecommendations`
<a name="personalize-runtime_GetRecommendations_java_2_topic"></a>

The following code example shows how to use `GetRecommendations`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/personalize#code-examples).
Get a list of recommended items.

```
    public static void getRecs(PersonalizeRuntimeClient personalizeRuntimeClient, String campaignArn, String userId) {

        try {
            GetRecommendationsRequest recommendationsRequest = GetRecommendationsRequest.builder()
                    .campaignArn(campaignArn)
                    .numResults(20)
                    .userId(userId)
                    .build();

            GetRecommendationsResponse recommendationsResponse = personalizeRuntimeClient
                    .getRecommendations(recommendationsRequest);
            List<PredictedItem> items = recommendationsResponse.itemList();
            for (PredictedItem item : items) {
                System.out.println("Item Id is : " + item.itemId());
                System.out.println("Item score is : " + item.score());
            }

        } catch (AwsServiceException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
Get a list of recommended items from a recommender created in a domain dataset group.

```
    public static void getRecs(PersonalizeRuntimeClient personalizeRuntimeClient, String recommenderArn,
            String userId) {

        try {
            GetRecommendationsRequest recommendationsRequest = GetRecommendationsRequest.builder()
                    .recommenderArn(recommenderArn)
                    .numResults(20)
                    .userId(userId)
                    .build();

            GetRecommendationsResponse recommendationsResponse = personalizeRuntimeClient
                    .getRecommendations(recommendationsRequest);
            List<PredictedItem> items = recommendationsResponse.itemList();

            for (PredictedItem item : items) {
                System.out.println("Item Id is : " + item.itemId());
                System.out.println("Item score is : " + item.score());
            }
        } catch (AwsServiceException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
Use a filter when requesting recommendations.

```
    public static void getFilteredRecs(PersonalizeRuntimeClient personalizeRuntimeClient,
            String campaignArn,
            String userId,
            String filterArn,
            String parameter1Name,
            String parameter1Value1,
            String parameter1Value2,
            String parameter2Name,
            String parameter2Value) {

        try {

            Map<String, String> filterValues = new HashMap<>();

            filterValues.put(parameter1Name, String.format("\"%1$s\",\"%2$s\"",
                    parameter1Value1, parameter1Value2));
            filterValues.put(parameter2Name, String.format("\"%1$s\"",
                    parameter2Value));

            GetRecommendationsRequest recommendationsRequest = GetRecommendationsRequest.builder()
                    .campaignArn(campaignArn)
                    .numResults(20)
                    .userId(userId)
                    .filterArn(filterArn)
                    .filterValues(filterValues)
                    .build();

            GetRecommendationsResponse recommendationsResponse = personalizeRuntimeClient
                    .getRecommendations(recommendationsRequest);
            List<PredictedItem> items = recommendationsResponse.itemList();

            for (PredictedItem item : items) {
                System.out.println("Item Id is : " + item.itemId());
                System.out.println("Item score is : " + item.score());
            }
        } catch (PersonalizeRuntimeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [GetRecommendations](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-runtime-2018-05-22/GetRecommendations) in *AWS SDK for Java 2.x API Reference*.
