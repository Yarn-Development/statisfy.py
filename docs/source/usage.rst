Usage
=============

Sample Python Code
------------------

    .. code-block:: python

        >> from "statisfy" import YouTube
        >> yt = YouTube("API_KEY")
        >> yt.getVideobyQuery("Niko Omilana") # returns json response
        >> vid = objectify(query)
        >> vid.id
        "VeYRaOV0I_Y"

JSON Response 
-------------

    .. code-block:: json

            {
            "kind": "youtube#video",
            "etag": "tF0xqPpwDiMU0YypLC2prUwq62M",
            "id": "VeYRaOV0I_Y",
            "snippet": {
                "publishedAt": "2022-09-05T18:27:48Z",
                "channelId": "UCdcUmdOxMrhRjKMw-BX19AA",
                "title": "SNEAKING Into KSI's Boxing Match (In the ring)",
                "description": "I pranked KSI and the whole internet by sneaking into his first boxing match in years, in a prime bottle mascot. Enjoy my friends.\nPls subscribe to Kysha- https://www.youtube.com/c/KyshaSwordy\nFollow me on Instagram- http://instagram.com/niko\nCourtesy of Dazn for all fight footage- https://www.dazn.com/\n\r\nBUY MY MERCH- https://www.shopndl.com/\r\nFollow me on Twitter- https://twitter.com/NikoOmilana\nMusic made by Miles- https://www.youtube.com/channel/UCy_bbwPsSwNmdlYpExi9fYQ\nDiscovery Song By Scott Buckley- https://youtu.be/VeYRaOV0I_Y\nSpecial mention to Batson- https://www.youtube.com/c/Batsonn\n\nBusiness Email - Nikoenquiries@gmail.com",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/VeYRaOV0I_Y/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/VeYRaOV0I_Y/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/VeYRaOV0I_Y/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    },
                    "standard": {
                        "url": "https://i.ytimg.com/vi/VeYRaOV0I_Y/sddefault.jpg",
                        "width": 640,
                        "height": 480
                    },
                    "maxres": {
                        "url": "https://i.ytimg.com/vi/VeYRaOV0I_Y/maxresdefault.jpg",
                        "width": 1280,
                        "height": 720
                    }
                },
                "channelTitle": "Niko Omilana",
                "categoryId": "24",
                "liveBroadcastContent": "none",
                "localized": {
                    "title": "SNEAKING Into KSI's Boxing Match (In the ring)",
                    "description": "I pranked KSI and the whole internet by sneaking into his first boxing match in years, in a prime bottle mascot. Enjoy my friends.\nPls subscribe to Kysha- https://www.youtube.com/c/KyshaSwordy\nFollow me on Instagram- http://instagram.com/niko\nCourtesy of Dazn for all fight footage- https://www.dazn.com/\n\r\nBUY MY MERCH- https://www.shopndl.com/\r\nFollow me on Twitter- https://twitter.com/NikoOmilana\nMusic made by Miles- https://www.youtube.com/channel/UCy_bbwPsSwNmdlYpExi9fYQ\nDiscovery Song By Scott Buckley- https://youtu.be/VeYRaOV0I_Y\nSpecial mention to Batson- https://www.youtube.com/c/Batsonn\n\nBusiness Email - Nikoenquiries@gmail.com"
                },
                "defaultAudioLanguage": "fr-FR"
            },
            "contentDetails": {
                "duration": "PT25M35S",
                "dimension": "2d",
                "definition": "hd",
                "caption": "false",
                "licensedContent": true,
                "contentRating": {},
                "projection": "rectangular"
            },
            "statistics": {
                "viewCount": "11818646",
                "likeCount": "1112557",
                "favoriteCount": "0",
                "commentCount": "19524"
            }
        }

