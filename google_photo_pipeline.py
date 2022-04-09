import pandas as pd
from google_photos_api import GooglePhotosApi

# CLIENT_SECRET_FILE = r'../credentials/client_secret_python_workflow.json'
# API_NAME = 'photoslibrary'
# API_VERSION = 'v1'
# SCOPES = ['https://www.googleapis.com/auth/photoslibrary']
#
# # service = google_photos_api.create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# # print("service:" + service)

google_photos_api = GooglePhotosApi()
service = google_photos_api.create_service()
# my_albums = service.albums().list().execute()
# my_albums_list = my_albums.get('albums')
media_items = service.mediaItems().search().execute()
df = pd.DataFrame(media_items)
pass
#
# """
# list method
# """
# response = service.mediaItems().list(pageSize=25).execute()
#
# lst_medias = response.get('mediaItems')
# nextPageToken = response.get('nextPageToken')
#
# while nextPageToken:
#     response = service.mediaItems().list(
#         pageSize=25,
#         pageToken=nextPageToken
#     ).execute()
#
#     lst_medias.extend(response.get('mediaItems'))
#     nextPageToken = response.get('nextPageToken')
#
# df_media_items = pd.DataFrame(lst_medias)
#
#
# """
# get method
# """
# media_id = df_media_items['id'][108]
# response = service.mediaItems().get(mediaItemId=media_id).execute()
#
#
# """
# batchGet method
# """
# media_ids = df_media_items['id'][107:112].to_list()
# response = service.mediaItems().batchGet(mediaItemIds=media_ids).execute()
# print(pd.DataFrame(response.get('mediaItemResults'))['mediaItem'].apply(pd.Series))
#
#
# """
# search method (by album id)
# """
# response_albums_list = service.albums().list().execute()
# albums_list = response_albums_list.get('albums')
#
# album_id = next(filter(lambda x: "Google Product Icons" in x['title'], albums_list))['id']
#
# request_body = {
#     'albumId': album_id,
#     'pageSize': 25
# }
#
# response_search = service.mediaItems().search(body=request_body).execute()
#
# lstMediaItems = response_search.get('mediaItems')
# nextPageToken = response_search.get('nextPageToken')
#
# while nextPageToken:
#     request_body['pageToken'] = nextPageToken
#
#     response_search = service.mediaItems().search(body=request_body).execute()
#     lstMediaItems.extend(response_search.get('mediaItems'))
#     nextPageToken = response_search.get('nextPageToken')
#
# df_search_result = pd.DataFrame(lstMediaItems)
#
#
# def response_media_items_by_filter(request_body: dict):
#     try:
#         response_search = service.mediaItems().search(body=request_body).execute()
#         lstMediaItems = response_search.get('mediaItems')
#         nextPageToken = response_search.get('nextPageToken')
#
#         while nextPageToken:
#             request_body['pageToken'] = nextPageToken
#             response_search = service.mediaItems().search(body=request_body).execute()
#
#             if not response_search.get('mediaItem') is None:
#                 lstMediaItems.extend(response_search.get('mediaItems'))
#                 nextPageToken = response_search.get('nextPageToken')
#             else:
#                 nextPageToken = ''
#         return lstMediaItems
#     except Exception as e:
#         print(e)
#         return None
#
# """
# search method (by date)
# """
# request_body = {
#     'pageSize': 100,
#     'filters': {
#         'dateFilter': {
#             # 'ranges': [
#             #     {
#             #         'startDate': {
#             #             'year': 2019,
#             #             'month': 1,
#             #             'day': 1
#             #         },
#             #         'endDate': {
#             #             'year': 2019,
#             #             'month': 12,
#             #             'day': 31
#             #         }
#             #     }
#             # ]
#             'dates': [
#                 {
#                     'year': 2019,
#                     'month': 12,
#                     'day': 23
#                 },
#                 {
#                     'year': 2019,
#                     'month': 11,
#                     'day': 19
#                 },
#                 {
#                     'year': 2019,
#                     'month': 11,
#                     'day': 20
#                 }
#             ]
#         }
#     }
# }
#
# df_search_result = pd.DataFrame(response_media_items_by_filter(request_body))
#
#
#
# """
# search method (content filter)
# """
# request_body = {
#     'pageSize': 100,
#     'filters': {
#         'contentFilter': {
#             'includedContentCategories': [
#                 'LANDMARKS', 'GARDENS'
#             ],
#             'excludedContentCategories': [
#                 'SPORT', 'ANIMALS'
#             ]
#         }
#     }
# }
#
# df_search_result = pd.DataFrame(response_media_items_by_filter(request_body))
#
#
# """
# search method (media type)
# """
# request_body = {
#     'pageSize': 100,
#     'filters': {
#         'mediaTypeFilter': {
#             'mediaTypes': ['VIDEO']
#         }
#     }
# }
#
# df_search_result = pd.DataFrame(response_media_items_by_filter(request_body))
#
#
# """
# search method (feature filter)
# """
# request_body = {
#     'pageSize': 100,
#     'filters': {
#         'featureFilter': {
#             'includedFeatures': ['FAVORITES']
#         }
#     }
# }
#
# df_search_result = pd.DataFrame(response_media_items_by_filter(request_body))
#
#
# """
# search method (includedArchiveMedia, excludedAppCreatedData)
# """
# request_body = {
#     'pageSize': 100,
#     'filters': {
#         'includeArchivedMedia': True,
#         'excludeNonAppCreatedData': False
#     }
# }
# df_search_result = pd.DataFrame(response_media_items_by_filter(request_body))