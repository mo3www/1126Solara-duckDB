import duckdb
import pandas as pd
import leafmap.maplibregl as leafmap


# con = duckdb.connect()
# 
# # 安裝和載入 httpfs (遠端檔案存取)
# con.install_extension("httpfs")
# con.load_extension("httpfs")
# 
# # 安裝和載入 spatial (用於空間資料處理)
# con.install_extension("spatial")
# con.load_extension("spatial")
# 
# print("DuckDB 連線建立，httpfs 和 spatial 擴充功能載入完成。")
# 
# url = "https://data.gishub.org/duckdb/nyc_data.db.zip"
# leafmap.download_file(url, unzip=True)
# con = duckdb.connect("nyc_data.db")
# # 為新建立的connection再安裝和載入 spatial (用於空間資料處理)
# con.install_extension("spatial")
# con.load_extension("spatial")
# 
# # 執行 SQL 查詢並將結果匯出為 Pandas DataFrame
# sql_select_wkt = "SELECT *, ST_AsText(geom) AS geometry FROM nyc_subway_stations limit 5"
# subway_stations_df = con.sql(sql_select_wkt).df()
# print("\n--- 查詢結果轉 Pandas DataFrame (含 WKT) ---")
# print(subway_stations_df)
# 
# gdf = leafmap.df_to_gdf(
#     subway_stations_df,
#     geometry="geometry", # 指定 WKT 欄位名稱
#     src_crs="EPSG:26918",
#     dst_crs="EPSG:4326"
# )
# 
# print("\n--- 轉換為 GeoDataFrame (Leafmap) ---")
# print(gdf.head())
# print(f"\nGeoDataFrame 的 CRS: {gdf.crs}")
# print("\n")

# 這裡報錯，說是版本不支援圖層設定
m = leafmap.Map(style="dark-matter")
m.add_basemap("Esri.WorldImagery")
m.add_data(
    gdf,
    column="OBJECTID",
    layer_type="circle",
    # legend=False,
    fill_color="#FFD700",
    radius=6,
    stroke_color="#FFFFFF",
    name="NYC Subway Stations"
)
m # 顯示地圖