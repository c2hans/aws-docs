---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-managedloginbranding.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::ManagedLoginBranding
<a name="aws-resource-cognito-managedloginbranding"></a>

Creates a new set of branding settings for a user pool style and associates it with an app client. This operation is the programmatic option for the creation of a new style in the branding designer.

Provides values for UI customization in a `Settings` JSON object and image files in an `Assets` array. To send the JSON object `Document` type parameter in `Settings`, you might need to update to the most recent version of your AWS SDK.

 This operation has a 2-megabyte request-size limit and include the CSS settings and image assets for your app client. Your branding settings might exceed 2MB in size. Amazon Cognito doesn't require that you pass all parameters in one request and preserves existing style settings that you don't specify. If your request is larger than 2MB, separate it into multiple requests, each with a size smaller than the limit.

As a best practice, modify the output of [DescribeManagedLoginBrandingByClient](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBrandingByClient.html) into the request parameters for this operation. To get all settings, set `ReturnMergedResources` to `true`. For more information, see [API and SDK operations for managed login branding](https://docs.aws.amazon.com/cognito/latest/developerguide/managed-login-brandingdesigner.html#branding-designer-api)

## Syntax
<a name="aws-resource-cognito-managedloginbranding-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-managedloginbranding-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::ManagedLoginBranding",
  "Properties" : {
      "[Assets](#cfn-cognito-managedloginbranding-assets)" : {{[ AssetType, ... ]}},
      "[ClientId](#cfn-cognito-managedloginbranding-clientid)" : {{String}},
      "[ReturnMergedResources](#cfn-cognito-managedloginbranding-returnmergedresources)" : {{Boolean}},
      "[Settings](#cfn-cognito-managedloginbranding-settings)" : {{Json}},
      "[UseCognitoProvidedValues](#cfn-cognito-managedloginbranding-usecognitoprovidedvalues)" : {{Boolean}},
      "[UserPoolId](#cfn-cognito-managedloginbranding-userpoolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-managedloginbranding-syntax.yaml"></a>

```
Type: AWS::Cognito::ManagedLoginBranding
Properties:
  [Assets](#cfn-cognito-managedloginbranding-assets): {{
    - AssetType}}
  [ClientId](#cfn-cognito-managedloginbranding-clientid): {{String}}
  [ReturnMergedResources](#cfn-cognito-managedloginbranding-returnmergedresources): {{Boolean}}
  [Settings](#cfn-cognito-managedloginbranding-settings): {{Json}}
  [UseCognitoProvidedValues](#cfn-cognito-managedloginbranding-usecognitoprovidedvalues): {{Boolean}}
  [UserPoolId](#cfn-cognito-managedloginbranding-userpoolid): {{String}}
```

## Properties
<a name="aws-resource-cognito-managedloginbranding-properties"></a>

`Assets`  <a name="cfn-cognito-managedloginbranding-assets"></a>
An array of image files that you want to apply to roles like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.
*Required*: No
*Type*: Array of [AssetType](aws-properties-cognito-managedloginbranding-assettype.md)
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-cognito-managedloginbranding-clientid"></a>
The app client that you want to assign the branding style to. Each style is linked to an app client until you delete it.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReturnMergedResources`  <a name="cfn-cognito-managedloginbranding-returnmergedresources"></a>
When `true`, returns values for branding options that are unchanged from Amazon Cognito defaults. When `false` or when you omit this parameter, returns only values that you customized in your branding style.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Settings`  <a name="cfn-cognito-managedloginbranding-settings"></a>
A JSON file, encoded as a `Document` type, with the the settings that you want to apply to your style.
The following components are not currently implemented and reserved for future use:
+  `signUp`
+  `instructions`
+  `sessionTimerDisplay`
+ `languageSelector` (for localization, see [Managed login localization)](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-localization)
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseCognitoProvidedValues`  <a name="cfn-cognito-managedloginbranding-usecognitoprovidedvalues"></a>
When true, applies the default branding style options. This option reverts to default style options that are managed by Amazon Cognito. You can modify them later in the branding editor.
When you specify `true` for this option, you must also omit values for `Settings` and `Assets` in the request.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-managedloginbranding-userpoolid"></a>
The user pool where the branding style is assigned.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-managedloginbranding-return-values"></a>

### Ref
<a name="aws-resource-cognito-managedloginbranding-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the style ID, for example `a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cognito-managedloginbranding-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cognito-managedloginbranding-return-values-fn--getatt-fn--getatt"></a>

`ManagedLoginBrandingId`  <a name="ManagedLoginBrandingId-fn::getatt"></a>
The ID of the managed login branding style.

## Examples
<a name="aws-resource-cognito-managedloginbranding--examples"></a>

### Creating a new branding style for an app client
<a name="aws-resource-cognito-managedloginbranding--examples--Creating_a_new_branding_style_for_an_app_client"></a>

The following example creates a branding style for the requested app client.

#### JSON
<a name="aws-resource-cognito-managedloginbranding--examples--Creating_a_new_branding_style_for_an_app_client--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Provision a managed login branding style to a user pool app client\n",
    "Resources": {
        "ManagedLoginBranding": {
            "Properties": {
                "Assets": [
                    {
                        "Bytes": "PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iNDAwIiB2aWV3Qm94PSIwIDAgMjAwMDAgNDAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyBjbGlwLXBhdGg9InVybCgjY2xpcDBfMTcyNTlfMjM2Njc0KSI+CjxyZWN0IHdpZHRoPSIyMDAwMCIgaGVpZ2h0PSI0MDAiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl8xNzI1OV8yMzY2NzQpIi8+CjxwYXRoIGQ9Ik0wIDBIMjAwMDBWNDAwSDBWMFoiIGZpbGw9IiMxMjIwMzciIGZpbGwtb3BhY2l0eT0iMC41Ii8+CjwvZz4KPGRlZnM+CjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8xNzI1OV8yMzY2NzQiIHgxPSItODk0LjI0OSIgeTE9IjE5OS45MzEiIHgyPSIxODAzNC41IiB5Mj0iLTU4OTkuNTciIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4KPHN0b3Agc3RvcC1jb2xvcj0iI0JGODBGRiIvPgo8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjhGQUIiLz4KPC9saW5lYXJHcmFkaWVudD4KPGNsaXBQYXRoIGlkPSJjbGlwMF8xNzI1OV8yMzY2NzQiPgo8cmVjdCB3aWR0aD0iMjAwMDAiIGhlaWdodD0iNDAwIiBmaWxsPSJ3aGl0ZSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=",
                        "Category": "PAGE_FOOTER_BACKGROUND",
                        "ColorMode": "DARK",
                        "Extension": "SVG"
                    }
                ],
                "ClientId": "1example23456789",
                "ReturnMergedResources": false,
                "Settings": {
                    "categories": {
                        "auth": {
                            "authMethodOrder": [
                                [
                                    {
                                        "display": "BUTTON",
                                        "type": "FEDERATED"
                                    },
                                    {
                                        "display": "INPUT",
                                        "type": "USERNAME_PASSWORD"
                                    }
                                ]
                            ],
                            "federation": {
                                "interfaceStyle": "BUTTON_LIST",
                                "order": [
                                ]
                            }
                        },
                        "form": {
                            "displayGraphics": true,
                            "instructions": {
                                "enabled": false
                            },
                            "languageSelector": {
                                "enabled": false
                            },
                            "location": {
                                "horizontal": "CENTER",
                                "vertical": "CENTER"
                            },
                            "sessionTimerDisplay": "NONE"
                        },
                        "global": {
                            "colorSchemeMode": "LIGHT",
                            "pageFooter": {
                                "enabled": false
                            },
                            "pageHeader": {
                                "enabled": false
                            },
                            "spacingDensity": "REGULAR"
                        },
                        "signUp": {
                            "acceptanceElements": [
                                {
                                    "enforcement": "NONE",
                                    "textKey": "en"
                                }
                            ]
                        }
                    },
                    "componentClasses": {
                        "buttons": {
                            "borderRadius": 8.0
                        },
                        "divider": {
                            "darkMode": {
                                "borderColor": "232b37ff"
                            },
                            "lightMode": {
                                "borderColor": "ebebf0ff"
                            }
                        },
                        "dropDown": {
                            "borderRadius": 8.0,
                            "darkMode": {
                                "defaults": {
                                    "itemBackgroundColor": "192534ff"
                                },
                                "hover": {
                                    "itemBackgroundColor": "081120ff",
                                    "itemBorderColor": "5f6b7aff",
                                    "itemTextColor": "e9ebedff"
                                },
                                "match": {
                                    "itemBackgroundColor": "d1d5dbff",
                                    "itemTextColor": "89bdeeff"
                                }
                            },
                            "lightMode": {
                                "defaults": {
                                    "itemBackgroundColor": "ffffffff"
                                },
                                "hover": {
                                    "itemBackgroundColor": "f4f4f4ff",
                                    "itemBorderColor": "7d8998ff",
                                    "itemTextColor": "000716ff"
                                },
                                "match": {
                                    "itemBackgroundColor": "414d5cff",
                                    "itemTextColor": "0972d3ff"
                                }
                            }
                        },
                        "focusState": {
                            "darkMode": {
                                "borderColor": "539fe5ff"
                            },
                            "lightMode": {
                                "borderColor": "0972d3ff"
                            }
                        },
                        "idpButtons": {
                            "icons": {
                                "enabled": true
                            }
                        },
                        "input": {
                            "borderRadius": 8.0,
                            "darkMode": {
                                "defaults": {
                                    "backgroundColor": "0f1b2aff",
                                    "borderColor": "5f6b7aff"
                                },
                                "placeholderColor": "8d99a8ff"
                            },
                            "lightMode": {
                                "defaults": {
                                    "backgroundColor": "ffffffff",
                                    "borderColor": "7d8998ff"
                                },
                                "placeholderColor": "5f6b7aff"
                            }
                        },
                        "inputDescription": {
                            "darkMode": {
                                "textColor": "8d99a8ff"
                            },
                            "lightMode": {
                                "textColor": "5f6b7aff"
                            }
                        },
                        "inputLabel": {
                            "darkMode": {
                                "textColor": "d1d5dbff"
                            },
                            "lightMode": {
                                "textColor": "000716ff"
                            }
                        },
                        "link": {
                            "darkMode": {
                                "defaults": {
                                    "textColor": "539fe5ff"
                                },
                                "hover": {
                                    "textColor": "89bdeeff"
                                }
                            },
                            "lightMode": {
                                "defaults": {
                                    "textColor": "0972d3ff"
                                },
                                "hover": {
                                    "textColor": "033160ff"
                                }
                            }
                        },
                        "optionControls": {
                            "darkMode": {
                                "defaults": {
                                    "backgroundColor": "0f1b2aff",
                                    "borderColor": "7d8998ff"
                                },
                                "selected": {
                                    "backgroundColor": "539fe5ff",
                                    "foregroundColor": "000716ff"
                                }
                            },
                            "lightMode": {
                                "defaults": {
                                    "backgroundColor": "ffffffff",
                                    "borderColor": "7d8998ff"
                                },
                                "selected": {
                                    "backgroundColor": "0972d3ff",
                                    "foregroundColor": "ffffffff"
                                }
                            }
                        },
                        "statusIndicator": {
                            "darkMode": {
                                "error": {
                                    "backgroundColor": "1a0000ff",
                                    "borderColor": "eb6f6fff",
                                    "indicatorColor": "eb6f6fff"
                                },
                                "pending": {
                                    "indicatorColor": "AAAAAAAA"
                                },
                                "success": {
                                    "backgroundColor": "001a02ff",
                                    "borderColor": "29ad32ff",
                                    "indicatorColor": "29ad32ff"
                                },
                                "warning": {
                                    "backgroundColor": "1d1906ff",
                                    "borderColor": "e0ca57ff",
                                    "indicatorColor": "e0ca57ff"
                                }
                            },
                            "lightMode": {
                                "error": {
                                    "backgroundColor": "fff7f7ff",
                                    "borderColor": "d91515ff",
                                    "indicatorColor": "d91515ff"
                                },
                                "pending": {
                                    "indicatorColor": "AAAAAAAA"
                                },
                                "success": {
                                    "backgroundColor": "f2fcf3ff",
                                    "borderColor": "037f0cff",
                                    "indicatorColor": "037f0cff"
                                },
                                "warning": {
                                    "backgroundColor": "fffce9ff",
                                    "borderColor": "8d6605ff",
                                    "indicatorColor": "8d6605ff"
                                }
                            }
                        }
                    },
                    "components": {
                        "alert": {
                            "borderRadius": 12.0,
                            "darkMode": {
                                "error": {
                                    "backgroundColor": "1a0000ff",
                                    "borderColor": "eb6f6fff"
                                }
                            },
                            "lightMode": {
                                "error": {
                                    "backgroundColor": "fff7f7ff",
                                    "borderColor": "d91515ff"
                                }
                            }
                        },
                        "favicon": {
                            "enabledTypes": [
                                "ICO",
                                "SVG"
                            ]
                        },
                        "form": {
                            "backgroundImage": {
                                "enabled": false
                            },
                            "borderRadius": 8.0,
                            "darkMode": {
                                "backgroundColor": "0f1b2aff",
                                "borderColor": "424650ff"
                            },
                            "lightMode": {
                                "backgroundColor": "ffffffff",
                                "borderColor": "c6c6cdff"
                            },
                            "logo": {
                                "enabled": false,
                                "formInclusion": "IN",
                                "location": "CENTER",
                                "position": "TOP"
                            }
                        },
                        "idpButton": {
                            "custom": {
                            },
                            "standard": {
                                "darkMode": {
                                    "active": {
                                        "backgroundColor": "354150ff",
                                        "borderColor": "89bdeeff",
                                        "textColor": "89bdeeff"
                                    },
                                    "defaults": {
                                        "backgroundColor": "0f1b2aff",
                                        "borderColor": "c6c6cdff",
                                        "textColor": "c6c6cdff"
                                    },
                                    "hover": {
                                        "backgroundColor": "192534ff",
                                        "borderColor": "89bdeeff",
                                        "textColor": "89bdeeff"
                                    }
                                },
                                "lightMode": {
                                    "active": {
                                        "backgroundColor": "d3e7f9ff",
                                        "borderColor": "033160ff",
                                        "textColor": "033160ff"
                                    },
                                    "defaults": {
                                        "backgroundColor": "ffffffff",
                                        "borderColor": "424650ff",
                                        "textColor": "424650ff"
                                    },
                                    "hover": {
                                        "backgroundColor": "f2f8fdff",
                                        "borderColor": "033160ff",
                                        "textColor": "033160ff"
                                    }
                                }
                            }
                        },
                        "pageBackground": {
                            "darkMode": {
                                "color": "0f1b2aff"
                            },
                            "image": {
                                "enabled": true
                            },
                            "lightMode": {
                                "color": "ffffffff"
                            }
                        },
                        "pageFooter": {
                            "backgroundImage": {
                                "enabled": false
                            },
                            "darkMode": {
                                "background": {
                                    "color": "0f141aff"
                                },
                                "borderColor": "424650ff"
                            },
                            "lightMode": {
                                "background": {
                                    "color": "fafafaff"
                                },
                                "borderColor": "d5dbdbff"
                            },
                            "logo": {
                                "enabled": false,
                                "location": "START"
                            }
                        },
                        "pageHeader": {
                            "backgroundImage": {
                                "enabled": false
                            },
                            "darkMode": {
                                "background": {
                                    "color": "0f141aff"
                                },
                                "borderColor": "424650ff"
                            },
                            "lightMode": {
                                "background": {
                                    "color": "fafafaff"
                                },
                                "borderColor": "d5dbdbff"
                            },
                            "logo": {
                                "enabled": false,
                                "location": "START"
                            }
                        },
                        "pageText": {
                            "darkMode": {
                                "bodyColor": "b6bec9ff",
                                "descriptionColor": "b6bec9ff",
                                "headingColor": "d1d5dbff"
                            },
                            "lightMode": {
                                "bodyColor": "414d5cff",
                                "descriptionColor": "414d5cff",
                                "headingColor": "000716ff"
                            }
                        },
                        "phoneNumberSelector": {
                            "displayType": "TEXT"
                        },
                        "primaryButton": {
                            "darkMode": {
                                "active": {
                                    "backgroundColor": "539fe5ff",
                                    "textColor": "000716ff"
                                },
                                "defaults": {
                                    "backgroundColor": "539fe5ff",
                                    "textColor": "000716ff"
                                },
                                "disabled": {
                                    "backgroundColor": "ffffffff",
                                    "borderColor": "ffffffff"
                                },
                                "hover": {
                                    "backgroundColor": "89bdeeff",
                                    "textColor": "000716ff"
                                }
                            },
                            "lightMode": {
                                "active": {
                                    "backgroundColor": "033160ff",
                                    "textColor": "ffffffff"
                                },
                                "defaults": {
                                    "backgroundColor": "0972d3ff",
                                    "textColor": "ffffffff"
                                },
                                "disabled": {
                                    "backgroundColor": "ffffffff",
                                    "borderColor": "ffffffff"
                                },
                                "hover": {
                                    "backgroundColor": "033160ff",
                                    "textColor": "ffffffff"
                                }
                            }
                        },
                        "secondaryButton": {
                            "darkMode": {
                                "active": {
                                    "backgroundColor": "354150ff",
                                    "borderColor": "89bdeeff",
                                    "textColor": "89bdeeff"
                                },
                                "defaults": {
                                    "backgroundColor": "0f1b2aff",
                                    "borderColor": "539fe5ff",
                                    "textColor": "539fe5ff"
                                },
                                "hover": {
                                    "backgroundColor": "192534ff",
                                    "borderColor": "89bdeeff",
                                    "textColor": "89bdeeff"
                                }
                            },
                            "lightMode": {
                                "active": {
                                    "backgroundColor": "d3e7f9ff",
                                    "borderColor": "033160ff",
                                    "textColor": "033160ff"
                                },
                                "defaults": {
                                    "backgroundColor": "ffffffff",
                                    "borderColor": "0972d3ff",
                                    "textColor": "0972d3ff"
                                },
                                "hover": {
                                    "backgroundColor": "f2f8fdff",
                                    "borderColor": "033160ff",
                                    "textColor": "033160ff"
                                }
                            }
                        }
                    }
                },
                "UseCognitoProvidedValues": false,
                "UserPoolId": "ca-central-1_EXAMPLE"
            },
            "Type": "AWS::Cognito::ManagedLoginBranding"
        }
    }
}
```

#### YAML
<a name="aws-resource-cognito-managedloginbranding--examples--Creating_a_new_branding_style_for_an_app_client--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"

Description: |
  Provision a managed login branding style to a user pool app client

Resources:
  ManagedLoginBranding:
    Type: AWS::Cognito::ManagedLoginBranding
    Properties:
      Assets:
        - Bytes: PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iNDAwIiB2aWV3Qm94PSIwIDAgMjAwMDAgNDAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyBjbGlwLXBhdGg9InVybCgjY2xpcDBfMTcyNTlfMjM2Njc0KSI+CjxyZWN0IHdpZHRoPSIyMDAwMCIgaGVpZ2h0PSI0MDAiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl8xNzI1OV8yMzY2NzQpIi8+CjxwYXRoIGQ9Ik0wIDBIMjAwMDBWNDAwSDBWMFoiIGZpbGw9IiMxMjIwMzciIGZpbGwtb3BhY2l0eT0iMC41Ii8+CjwvZz4KPGRlZnM+CjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8xNzI1OV8yMzY2NzQiIHgxPSItODk0LjI0OSIgeTE9IjE5OS45MzEiIHgyPSIxODAzNC41IiB5Mj0iLTU4OTkuNTciIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4KPHN0b3Agc3RvcC1jb2xvcj0iI0JGODBGRiIvPgo8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjhGQUIiLz4KPC9saW5lYXJHcmFkaWVudD4KPGNsaXBQYXRoIGlkPSJjbGlwMF8xNzI1OV8yMzY2NzQiPgo8cmVjdCB3aWR0aD0iMjAwMDAiIGhlaWdodD0iNDAwIiBmaWxsPSJ3aGl0ZSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=
          Category: PAGE_FOOTER_BACKGROUND
          ColorMode: DARK
          Extension: SVG
      ClientId: 1example23456789
      ReturnMergedResources: false
      Settings:
        categories:
          auth:
            authMethodOrder:
              - - display: BUTTON
                  type: FEDERATED
                - display: INPUT
                  type: USERNAME_PASSWORD
            federation:
              interfaceStyle: BUTTON_LIST
              order: []
          form:
            displayGraphics: true
            instructions:
              enabled: false
            languageSelector:
              enabled: false
            location:
              horizontal: CENTER
              vertical: CENTER
            sessionTimerDisplay: NONE
          global:
            colorSchemeMode: LIGHT
            pageFooter:
              enabled: false
            pageHeader:
              enabled: false
            spacingDensity: REGULAR
          signUp:
            acceptanceElements:
              - enforcement: NONE
                textKey: en
        componentClasses:
          buttons:
            borderRadius: 8.0
          divider:
            darkMode:
              borderColor: 232b37ff
            lightMode:
              borderColor: ebebf0ff
          dropDown:
            borderRadius: 8.0
            darkMode:
              defaults:
                itemBackgroundColor: 192534ff
              hover:
                itemBackgroundColor: 081120ff
                itemBorderColor: 5f6b7aff
                itemTextColor: e9ebedff
              match:
                itemBackgroundColor: d1d5dbff
                itemTextColor: 89bdeeff
            lightMode:
              defaults:
                itemBackgroundColor: ffffffff
              hover:
                itemBackgroundColor: f4f4f4ff
                itemBorderColor: 7d8998ff
                itemTextColor: 000716ff
              match:
                itemBackgroundColor: 414d5cff
                itemTextColor: 0972d3ff
          focusState:
            darkMode:
              borderColor: 539fe5ff
            lightMode:
              borderColor: 0972d3ff
          idpButtons:
            icons:
              enabled: true
          input:
            borderRadius: 8.0
            darkMode:
              defaults:
                backgroundColor: 0f1b2aff
                borderColor: 5f6b7aff
              placeholderColor: 8d99a8ff
            lightMode:
              defaults:
                backgroundColor: ffffffff
                borderColor: 7d8998ff
              placeholderColor: 5f6b7aff
          inputDescription:
            darkMode:
              textColor: 8d99a8ff
            lightMode:
              textColor: 5f6b7aff
          inputLabel:
            darkMode:
              textColor: d1d5dbff
            lightMode:
              textColor: 000716ff
          link:
            darkMode:
              defaults:
                textColor: 539fe5ff
              hover:
                textColor: 89bdeeff
            lightMode:
              defaults:
                textColor: 0972d3ff
              hover:
                textColor: 033160ff
          optionControls:
            darkMode:
              defaults:
                backgroundColor: 0f1b2aff
                borderColor: 7d8998ff
              selected:
                backgroundColor: 539fe5ff
                foregroundColor: 000716ff
            lightMode:
              defaults:
                backgroundColor: ffffffff
                borderColor: 7d8998ff
              selected:
                backgroundColor: 0972d3ff
                foregroundColor: ffffffff
          statusIndicator:
            darkMode:
              error:
                backgroundColor: 1a0000ff
                borderColor: eb6f6fff
                indicatorColor: eb6f6fff
              pending:
                indicatorColor: AAAAAAAA
              success:
                backgroundColor: 001a02ff
                borderColor: 29ad32ff
                indicatorColor: 29ad32ff
              warning:
                backgroundColor: 1d1906ff
                borderColor: e0ca57ff
                indicatorColor: e0ca57ff
            lightMode:
              error:
                backgroundColor: fff7f7ff
                borderColor: d91515ff
                indicatorColor: d91515ff
              pending:
                indicatorColor: AAAAAAAA
              success:
                backgroundColor: f2fcf3ff
                borderColor: 037f0cff
                indicatorColor: 037f0cff
              warning:
                backgroundColor: fffce9ff
                borderColor: 8d6605ff
                indicatorColor: 8d6605ff
        components:
          alert:
            borderRadius: 12.0
            darkMode:
              error:
                backgroundColor: 1a0000ff
                borderColor: eb6f6fff
            lightMode:
              error:
                backgroundColor: fff7f7ff
                borderColor: d91515ff
          favicon:
            enabledTypes:
              - ICO
              - SVG
          form:
            backgroundImage:
              enabled: false
            borderRadius: 8.0
            darkMode:
              backgroundColor: 0f1b2aff
              borderColor: 424650ff
            lightMode:
              backgroundColor: ffffffff
              borderColor: c6c6cdff
            logo:
              enabled: false
              formInclusion: IN
              location: CENTER
              position: TOP
          idpButton:
            custom: {}
            standard:
              darkMode:
                active:
                  backgroundColor: 354150ff
                  borderColor: 89bdeeff
                  textColor: 89bdeeff
                defaults:
                  backgroundColor: 0f1b2aff
                  borderColor: c6c6cdff
                  textColor: c6c6cdff
                hover:
                  backgroundColor: 192534ff
                  borderColor: 89bdeeff
                  textColor: 89bdeeff
              lightMode:
                active:
                  backgroundColor: d3e7f9ff
                  borderColor: 033160ff
                  textColor: 033160ff
                defaults:
                  backgroundColor: ffffffff
                  borderColor: 424650ff
                  textColor: 424650ff
                hover:
                  backgroundColor: f2f8fdff
                  borderColor: 033160ff
                  textColor: 033160ff
          pageBackground:
            darkMode:
              color: 0f1b2aff
            image:
              enabled: true
            lightMode:
              color: ffffffff
          pageFooter:
            backgroundImage:
              enabled: false
            darkMode:
              background:
                color: 0f141aff
              borderColor: 424650ff
            lightMode:
              background:
                color: fafafaff
              borderColor: d5dbdbff
            logo:
              enabled: false
              location: START
          pageHeader:
            backgroundImage:
              enabled: false
            darkMode:
              background:
                color: 0f141aff
              borderColor: 424650ff
            lightMode:
              background:
                color: fafafaff
              borderColor: d5dbdbff
            logo:
              enabled: false
              location: START
          pageText:
            darkMode:
              bodyColor: b6bec9ff
              descriptionColor: b6bec9ff
              headingColor: d1d5dbff
            lightMode:
              bodyColor: 414d5cff
              descriptionColor: 414d5cff
              headingColor: 000716ff
          phoneNumberSelector:
            displayType: TEXT
          primaryButton:
            darkMode:
              active:
                backgroundColor: 539fe5ff
                textColor: 000716ff
              defaults:
                backgroundColor: 539fe5ff
                textColor: 000716ff
              disabled:
                backgroundColor: ffffffff
                borderColor: ffffffff
              hover:
                backgroundColor: 89bdeeff
                textColor: 000716ff
            lightMode:
              active:
                backgroundColor: 033160ff
                textColor: ffffffff
              defaults:
                backgroundColor: 0972d3ff
                textColor: ffffffff
              disabled:
                backgroundColor: ffffffff
                borderColor: ffffffff
              hover:
                backgroundColor: 033160ff
                textColor: ffffffff
          secondaryButton:
            darkMode:
              active:
                backgroundColor: 354150ff
                borderColor: 89bdeeff
                textColor: 89bdeeff
              defaults:
                backgroundColor: 0f1b2aff
                borderColor: 539fe5ff
                textColor: 539fe5ff
              hover:
                backgroundColor: 192534ff
                borderColor: 89bdeeff
                textColor: 89bdeeff
            lightMode:
              active:
                backgroundColor: d3e7f9ff
                borderColor: 033160ff
                textColor: 033160ff
              defaults:
                backgroundColor: ffffffff
                borderColor: 0972d3ff
                textColor: 0972d3ff
              hover:
                backgroundColor: f2f8fdff
                borderColor: 033160ff
                textColor: 033160ff
      UseCognitoProvidedValues: false
      UserPoolId: ca-central-1_EXAMPLE
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
