from taipy import Gui
import taipy.gui.builder as tgb

# Add a navbar to switch from one page to the other
with tgb.Page() as root_page:
    tgb.navbar()
    tgb.text("# Oil spill detector", mode="md")

with tgb.Page() as page_1:
    tgb.text("## Problem statement", mode="md")
    tgb.text("A major bridge collapse in Baltimore caused an oil spill in \
    the Patapsco River, posing severe environmental threats.\
    Oil spills from the bridge collapse incident harm the\
    environment by releasing toxic compounds that poison and suffocate\
    marine life, damage sensitive ecosystems like wetlands and shorelines,\
    and contaminate water sources, causing long-lasting ecological devastation.")
    
    #put some image here idk
    tgb.image('bridge.jpg', label="bridge")


    tgb.text("We urgently need a tool that will help efficiently detect and\
    clean up the enviormental mess that this incideint has caused")
    



with tgb.Page() as page_2:
    #insert logo somewhere idk

    tgb.text("## This is page 2", mode="md")
    tgb.text("# Our solution", mode="md")
    tgb.text("That's why we made (name of our project), an AI tool that\
    automatically detects oil spills in a large area of water when given\
    an image. It will highlight the contaminated area, streamlining the\
    clean-up process.")
    tgb.text("We used Microsoft Education/azure as our main development\
    tool for our AI model, we trained and deployed it using (whatever\
    specific tools we used in Azure")
    tgb.text("Tradition methods such as checking the area by physically\
    scooping up water from a specific area and testing it with chemicals\
    to check if it contains oil spills take an unnecessarily large amount\
    of time and resources, such as people, tools, and chemicals. Whereas\
    our method of just taking a picture to detect where oil spills in water\
    are is much faster and cheaper.")


with tgb.Page() as page_3:
    tgb.text("test", mode="raw")
    tgb.text("test", raw=True)

pages = {
    "/": root_page,
    "page1": page_1,
    "page2": page_2,
    "page3": page_3
}

Gui(pages=pages).run(port=3000)