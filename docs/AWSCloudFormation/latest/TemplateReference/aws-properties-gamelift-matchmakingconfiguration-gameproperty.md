---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::MatchmakingConfiguration GameProperty
<a name="aws-properties-gamelift-matchmakingconfiguration-gameproperty"></a>

This key-value pair can store custom data about a game session. For example, you might use a `GameProperty` to track a game session's map, level of difficulty, or remaining time. The difficulty level could be specified like this: `{"Key": "difficulty", "Value":"Novice"}`.

 You can set game properties when creating a game session. You can also modify game properties of an active game session. When searching for game sessions, you can filter on game property keys and values. You can't delete game properties from a game session.

For examples of working with game properties, see [Create a game session with properties](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties).

## Syntax
<a name="aws-properties-gamelift-matchmakingconfiguration-gameproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-matchmakingconfiguration-gameproperty-syntax.json"></a>

```
{
  "[Key](#cfn-gamelift-matchmakingconfiguration-gameproperty-key)" : {{String}},
  "[Value](#cfn-gamelift-matchmakingconfiguration-gameproperty-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-matchmakingconfiguration-gameproperty-syntax.yaml"></a>

```
  [Key](#cfn-gamelift-matchmakingconfiguration-gameproperty-key): {{String}}
  [Value](#cfn-gamelift-matchmakingconfiguration-gameproperty-value): {{String}}
```

## Properties
<a name="aws-properties-gamelift-matchmakingconfiguration-gameproperty-properties"></a>

`Key`  <a name="cfn-gamelift-matchmakingconfiguration-gameproperty-key"></a>
The game property identifier.
+ Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.
+ If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.
*Required*: Yes
*Type*: String
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-gamelift-matchmakingconfiguration-gameproperty-value"></a>
The game property value.
*Required*: Yes
*Type*: String
*Maximum*: `96`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-gamelift-matchmakingconfiguration-gameproperty--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [Design a FlexMatch matchmaker](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html) in the *Amazon GameLift Developer Guide*
+ [GameProperty](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameProperty.html) in the *Amazon GameLift API Reference*
