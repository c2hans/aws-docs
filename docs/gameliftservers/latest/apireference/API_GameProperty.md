---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameProperty.html
---

# GameProperty
<a name="API_GameProperty"></a>

This key-value pair can store custom data about a game session. For example, you might use a `GameProperty` to track a game session's map, level of difficulty, or remaining time. The difficulty level could be specified like this: `{"Key": "difficulty", "Value":"Novice"}`.

 You can set game properties when creating a game session. You can also modify game properties of an active game session. When searching for game sessions, you can filter on game property keys and values. You can't delete game properties from a game session.

For examples of working with game properties, see [Create a game session with properties](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties).

## Contents
<a name="API_GameProperty_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="gameliftservers-Type-GameProperty-Key"></a>
The game property identifier.
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** Value **   <a name="gameliftservers-Type-GameProperty-Value"></a>
The game property value.
Type: String
Length Constraints: Maximum length of 96.
Required: Yes

## See Also
<a name="API_GameProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameProperty)
