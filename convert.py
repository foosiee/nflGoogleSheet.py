with open("matchup.txt") as f:
    content = f.read()

    if "Indianapolis" in content:
        content = content.replace("Indianapolis","IND")
    if "New England" in content:
        content = content.replace("New England","NE")
    if "Tennessee" in content:
        content = content.replace("Tennessee","TEN")
    if "Buffalo" in content:
        content = content.replace("Buffalo","BUF")
    if "Atlanta" in content:
        content = content.replace("Atlanta","ATL")
    if "Pittsburgh" in content:
        content = content.replace("Pittsburgh","PIT")
    if "Denver" in content:
        content = content.replace("Denver","DEN")
    if "NY Jets" in content:
        content = content.replace("NY Jets","NYJ")
    if "Jacksonville" in content:
        content = content.replace("Jacksonville","JAX")
    if "Kansas City" in content:
        content = content.replace("Kansas City", "KC")
    if "Green Bay" in content:
        content = content.replace("Green Bay","GB")
    if "Detroit" in content:
        content = content.replace("Detroit","DET")
    if "Baltimore" in content:
        content = content.replace("Baltimore","BAL")
    if "Cleveland" in content:
        content = content.replace("Cleveland","CLE")
    if "NY Giants" in content:
        content = content.replace("NY Giants","NYG")
    if "Carolina" in content:
        content = content.replace("Carolina","CAR")
    if "Miami" in content:
        content = content.replace("Miami","MIA")
    if "Cincinnati" in content:
        content = content.replace("Cincinnati","CIN")
    if "Oakland" in content:
        content = content.replace("Oakland","OAK")
    if "Los Angeles" in content:
        content = content.replace("Los Angeles","LA-")
    if "Arizona" in content:
        content = content.replace("Arizona","ARI")
    if "San Francisco" in content:
        content = content.replace("San Francisco","SF")
    if "Minnesota" in content:
        content = content.replace("Minnesota","MIN")
    if "Philadelphia" in content:
        content = content.replace("Philadelphia","PHI")
    if "Seattle" in content:
        content = content.replace("Seattle","SEA")
    if "Dallas" in content:
        content = content.replace("Dallas","DAL")
    if "Houston" in content:
        content = content.replace("Houston","HOU")
    if "Washington" in content:
        content = content.replace("Washington","WAS")
    if "New Orleans" in content:
        content = content.replace("New Orleans","NO")
print content
format = open("format.txt","w")
format.write(content)
