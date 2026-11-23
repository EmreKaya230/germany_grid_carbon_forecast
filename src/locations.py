# Weather locations: 3 x 3 grid over Germany, giving 9 land points, plus 2 offshore points.
# I used the cell centers. For nw, sw and se the center was outside Germany or in the sea,
# so I used a point inside the German land part of the cell instead.
LOCATIONS = {
    "nw" : (53.26, 8.12), # around Oldenburg , Lower Saxony
    "n" : (53.703, 10.503), # south of Lübeck, Schleswig-Holstein
    "ne" : (53.703, 13.512), # Mecklenburg-Vorpommern
    "w" : (51.143, 7.493), # Sauerland, NRW
    "center": (51.143, 10.503), # around Thüringen, Mühlhausen
    "e" : (51.143, 13.512), # northwest of Dresden, Saxony
    "sw" : (48.675, 8.422), # Nordschwarzwald , Baden-Württemberg
    "s" : (48.583, 10.503), # Swabia, Bavaria
    "se" : (48.647, 12.714), # Lower Bavaria
    "offshore_north_sea" : (54.0, 6.6), # North Sea
    "offshore_baltic" : (54.7, 13.0), #Baltic Sea
}

#print(len(LOCATIONS))