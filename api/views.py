from django.http.response import JsonResponse, HttpResponseRedirect

from rest_framework.views import APIView
from agoraapi.src.RtcTokenBuilder import RtcTokenBuilder
import time
import random



class AgoraToken(APIView):
    """
    Create agora api token by taking appid appcertificate and channelname
    post data like {"appid":"3926954451e5462e91010a3d5adeb698",
                    "appcertificate":"011b36047c1b45febab6799d2b5f6a33",
                    "channelname":"aurigait"}
    get responce like {
                        "appID": "3926954451e5462e91010a3d5adeb698",
                        "channelName": "aurigait",
                        "token": "0063926954451e5462e91010a3d5adeb698IABdRQlA1ilFWBvc6mvTlp3Sv0bRuHkt1dNXVOUzjFjl6lAySBkAAAAACgCj2iACsNTSYgAA"
                        }
    """

    def post(self, request, *args, **kwargs):
        data=request.data
        appID = data.get("appid",None)
        appCertificate = data.get("appcertificate",None)
        channelName = data.get("channelname",None)

        if appID is None or appCertificate is None or channelName is None:
            return JsonResponse({"status":"fail the value cant be None","appID":appID,"channelName":channelName,"token":token})

        token = RtcTokenBuilder.buildToken(appID, appCertificate, channelName)
        return JsonResponse({"appID":appID,"channelName":channelName,"token":token})
        