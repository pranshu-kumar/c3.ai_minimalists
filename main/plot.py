import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import geopandas as gpd
import contextily as ctx

path_state_vul = "../json/State_polygon_vulnerability_.json"
path_road_vul = "../json/State_road_vulnerability_upd.json"
path_centroid_vul = "../json/state_centroid_vulnerability.json"
path_air_transport_vul = "../json/State_air_transport_vulnerab.json"
path_air_state_vul = "../json/State_airport_vulnerability_.json"


'''
Plot Social Vulnerability
'''
def plot_state_social_vul(path):
    
    # Read json file and set epsg to 3857
    df = gpd.read_file(path)
    df = df.to_crs(epsg=3857)

    # Adding Colours to the states
    colors = []
    for vul in df['Social_vul']:
        # print(vul)
        if round(vul,3) <= 0.104 and round(vul,3) >= 0.0:
            colors.append("#c78ff7") # Light Purple
        elif round(vul,3) <= 0.239 and round(vul,3) >= 0.105:
            colors.append("#1f418f") # Dark Blue
        elif round(vul,3) <= 0.359 and round(vul,3) >= 0.240:
            colors.append("#24adbd") # Light Blue
        elif round(vul,3) <= 0.535 and round(vul,3) >= 0.360:
            colors.append("#16d933") # Light Green
        elif round(vul,3) <= 0.777 and round(vul,3) >= 0.536:
            colors.append("#cfd916") # Yellow
        elif round(vul,3) <= 1.0 and round(vul,3) >= 0.778:
            colors.append("#e32f0b") # Red
        else:
            print(vul)

    # print(colors)
    df['colors'] = colors

    ax = df.plot(color=df['colors'], figsize=(10,10), edgecolor='black', linewidth=0.7)
    
    # Adding names to the states
    df['coords'] = df['geometry'].apply(lambda x: x.representative_point().coords[:])
    df['coords'] = [coords[0] for coords in df['coords']]

    for idx, row in df.iterrows():
        plt.annotate(s=row['NAME'], xy=row['coords'],
                    horizontalalignment='center', size=8)

    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    
    # Legend Elements
    legend_elements = [
        Patch(facecolor='#c78ff7', label='0.000-0.104'),
        Patch(facecolor='#1f418f', label='0.105-0.239'),
        Patch(facecolor='#24adbd', label='0.240-0.359'),
        Patch(facecolor='#16d933', label='0.360-0.535'),
        Patch(facecolor='#cfd916', label='0.536-0.777'),
        Patch(facecolor='#e32f0b', label='0.778-1.000')
    ]
    plt.legend(handles=legend_elements, title="Social Vulnerability")
    
    plt.show()
    
'''
Plot Health Vulnerability
'''
def plot_state_health_vul(path):
    
    # Read json file and set epsg to 3857
    df = gpd.read_file(path)
    df = df.to_crs(epsg=3857)

    # Adding Colours to the states
    colors = []
    for vul in df['health_vul']:
        # print(vul)
        if round(vul,3) <= 0.104 and round(vul,3) >= 0.0:
            colors.append("#772eff") # Light Purple
        elif round(vul,3) <= 0.239 and round(vul,3) >= 0.105:
            colors.append("#1f418f") # Dark Blue
        elif round(vul,3) <= 0.359 and round(vul,3) >= 0.240:
            colors.append("#24adbd") # Light Blue
        elif round(vul,3) <= 0.535 and round(vul,3) >= 0.360:
            colors.append("#16d933") # Light Green
        elif round(vul,3) <= 0.777 and round(vul,3) >= 0.536:
            colors.append("#cfd916") # Yellow
        elif round(vul,3) <= 1.0 and round(vul,3) >= 0.778:
            colors.append("#e32f0b") # Red
        else:
            print(vul)

    # print(colors)
    df['colors'] = colors

    ax = df.plot(color=df['colors'], figsize=(10,10), edgecolor='black', linewidth=0.7)
    
    # Adding names to the states
    df['coords'] = df['geometry'].apply(lambda x: x.representative_point().coords[:])
    df['coords'] = [coords[0] for coords in df['coords']]

    for idx, row in df.iterrows():
        plt.annotate(s=row['NAME'], xy=row['coords'],
                    horizontalalignment='center', size=8)

    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    
    # Legend Elements
    legend_elements = [
        Patch(facecolor='#772eff', label='0.000-0.104'),
        Patch(facecolor='#1f418f', label='0.105-0.239'),
        Patch(facecolor='#24adbd', label='0.240-0.359'),
        Patch(facecolor='#16d933', label='0.360-0.535'),
        Patch(facecolor='#cfd916', label='0.536-0.777'),
        Patch(facecolor='#e32f0b', label='0.778-1.000')
    ]
    plt.legend(handles=legend_elements, title="Health Vulnerability")
    
    plt.show()


'''
Plot Total Vulnerability
'''
def plot_state_total_vul(path):

        # Read json file and set epsg to 3857
    df = gpd.read_file(path)
    df = df.to_crs(epsg=3857)

    # Adding Colours to the states
    colors = []
    for vul in df['Total_vul']:
        # print(vul)
        if round(vul,3) <= 0.104 and round(vul,3) >= 0.0:
            colors.append("#772eff") # Light Purple
        elif round(vul,3) <= 0.239 and round(vul,3) >= 0.105:
            colors.append("#1f418f") # Dark Blue
        elif round(vul,3) <= 0.359 and round(vul,3) >= 0.240:
            colors.append("#24adbd") # Light Blue
        elif round(vul,3) <= 0.535 and round(vul,3) >= 0.360:
            colors.append("#16d933") # Light Green
        elif round(vul,3) <= 0.777 and round(vul,3) >= 0.536:
            colors.append("#cfd916") # Yellow
        elif round(vul,3) <= 1.0 and round(vul,3) >= 0.778:
            colors.append("#e32f0b") # Red
        else:
            print(vul)

    # print(colors)
    df['colors'] = colors

    ax = df.plot(color=df['colors'], figsize=(10,10), edgecolor='black', linewidth=0.7)
    
    # Adding names to the states
    df['coords'] = df['geometry'].apply(lambda x: x.representative_point().coords[:])
    df['coords'] = [coords[0] for coords in df['coords']]

    for idx, row in df.iterrows():
        plt.annotate(s=row['NAME'], xy=row['coords'],
                    horizontalalignment='center', size=8)

    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    
    # Legend Elements
    legend_elements = [
        Patch(facecolor='#772eff', label='0.000-0.104'),
        Patch(facecolor='#1f418f', label='0.105-0.239'),
        Patch(facecolor='#24adbd', label='0.240-0.359'),
        Patch(facecolor='#16d933', label='0.360-0.535'),
        Patch(facecolor='#cfd916', label='0.536-0.777'),
        Patch(facecolor='#e32f0b', label='0.778-1.000')
    ]
    plt.legend(handles=legend_elements, title="Total Vulnerability")
    
    plt.show()

'''
Plot Road Networks Vulnerability
'''
def plot_state_road_vul(road_path, state_path, centroid_path):
    
    # Read json file and set epsg to 3857
    road_df = gpd.read_file(road_path)
    road_df = road_df.to_crs(epsg=3857)
    state_df = gpd.read_file(state_path)
    state_df = state_df.to_crs(epsg=3857)
    centroid_df = gpd.read_file(centroid_path)
    centroid_df = centroid_df.to_crs(epsg=3857)

    # Adding colour to the paths
    colors = []
    for vul in road_df['wt_ij']:
        # print(vul)
        if round(vul,3) <= 0.094 and round(vul,3) >= 0.0:
            colors.append("#1f418f") # Dark Blue
        elif round(vul,3) <= 0.194 and round(vul,3) >= 0.095:
            colors.append("#24adbd") # Light Blue
        elif round(vul,3) <= 0.308 and round(vul,3) >= 0.195:
            colors.append("#16d933") # Light Green
        elif round(vul,3) <= 0.497 and round(vul,3) >= 0.309:
            colors.append("#cfd916") # Yellow
        elif round(vul,3) <= 1 and round(vul,3) >= 0.498:
            colors.append("#e32f0b") # Red    
        else:
            print(vul)

    road_df['colors'] = colors

    # Adding colors for the centroids
    colors_centroid = []
    for vul in state_df['Total_vul']:
        if round(vul,3) <= 0.094 and round(vul,3) >= 0.0:
            colors_centroid.append("#1f418f") # Dark Blue
        elif round(vul,3) <= 0.194 and round(vul,3) >= 0.095:
            colors_centroid.append("#24adbd") # Light Blue
        elif round(vul,3) <= 0.308 and round(vul,3) >= 0.195:
            colors_centroid.append("#16d933") # Light Green
        elif round(vul,3) <= 0.497 and round(vul,3) >= 0.309:
            colors_centroid.append("#cfd916") # Yellow
        elif round(vul,3) <= 1 and round(vul,3) >= 0.498:
            colors_centroid.append("#e32f0b") # Red    
        else:
            print(vul)

    # print(len(colors_centroid))
    centroid_df['colors'] = colors_centroid


    # Legend Elements
    legend_elements_network = [
        Line2D([0], [0], color='#24adbd', lw=1, label='0.000 - 0.094'),
        Line2D([0], [0], color='#1f418f', lw=1, label='0.095 - 0.194'),
        Line2D([0], [0], color='#16d933', lw=1, label='0.195 - 0.308'),
        Line2D([0], [0], color='#cfd916', lw=1, label='0.309 - 0.497'),
        Line2D([0], [0], color='#e32f0b', lw=1, label='0.498 - 1'),
    ]

    legend_elements_centroid = [
        Line2D([0], [0], marker='o',color='white', label='0.000 - 0.094',markerfacecolor='#1f418f', markersize=15),
        Line2D([0], [0], marker='o',color='white', label='0.095 - 0.194',markerfacecolor='#24adbd', markersize=15),
        Line2D([0], [0], marker='o',color='white', label='0.195 - 0.308',markerfacecolor='#16d933', markersize=15),
        Line2D([0], [0], marker='o',color='white', label='0.309 - 0.497',markerfacecolor='#cfd916', markersize=15),
        Line2D([0], [0], marker='o',color='white', label='0.498 - 1',markerfacecolor='#e32f0b', markersize=15),   
    ]


    
    base = state_df.boundary.plot(color='black', linewidth=0.8)
    
    # Adding names to the states
    state_df['coords'] = state_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    state_df['coords'] = [coords[0] for coords in state_df['coords']]

    for idx, row in state_df.iterrows():
        plt.annotate(s=row['NAME'], xy=row['coords'],
                    horizontalalignment='center', size=8)

    # Plotting
    ctx.add_basemap(base, source=ctx.providers.Stamen.TerrainBackground)
    centroid_plot = centroid_df.plot(ax=base, color=centroid_df['colors'], linewidth=4)
    road_plot = road_df.plot(ax=centroid_plot,color=road_df['colors'], figsize=(10,10), linewidth=2)
    legend_network = plt.legend(handles=legend_elements_network, title="Road Networks Vulnerability", loc='lower right')
    legend_centroid = plt.legend(handles=legend_elements_centroid, title="Total Vulnerability", loc='upper right')
    road_plot.add_artist(legend_network)
    road_plot.add_artist(legend_centroid)
    plt.show()

'''
Plot Air Transport Vulnerability
'''
def plot_air_transport_vul():
    pass

# plot_state_road_vul(path_road_vul, path_state_vul, path_centroid_vul)
# plot_state_total_vul(path_state_vul)