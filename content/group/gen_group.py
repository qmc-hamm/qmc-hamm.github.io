def member_format(m):
    return """ <tr> <td width="15%%"> <img src="/images/%s"> </td>
<td> <span id="bioname"> <b> %s </b> </span>  <br>
%s
<p> %s </p>
</td>
</tr>""" % (
        m["image"],
        m["name"],
        m["position"],
        m["description"],
    )


members = [
    {
        "name": "Lucas Wagner",
        "position": "Director",
        "image": "wagner.jpg",
        "description": """Multiscale quantum models""",
    },
    {
        "name": "David Ceperley",
        "position": "co-PI",
        "image": "ceperley.jpg",
        "description": """Quantum Monte Carlo, High pressure hydrogen""",
    },
    {
        "name": "Harley Johnson",
        "position": "co-PI",
        "image": "harley.jpg",
        "description": """Tight binding""",
    },
    {
        "name": "Elif Ertekin",
        "position": "co-PI",
        "image": "elif.jpg",
        "description": """Uncertainty quantification""",
    },
    {
        "name": "Ben Galewsky",
        "position": "Software and data engineer",
        "image": "profile-placeholder.gif",
        "description": """Ben is helping with workflows and data publication.""",
    },
        {
        "name": "Tawfiqur Rakib",
        "position": "Postdoctoral Associate",
        "image": "tawfiq.jpg",
        "description": """Tawfiq is working on uncertainty quantification.""",
    },
            {
        "name": "Jeonghwan Ahn",
        "position": "Postdoctoral Associate",
        "image": "jeonghwan.jpg",
        "description": """Jeonghwan is working on using quantum Monte Carlo for learning quantum models.""",
    },

        {
        "name": "Young-Jae Choi",
        "position": "Postdoctoral Associate",
        "image": "youngjae.jpg",
        "description": """Young-Jae is working on uncertainty quantification of machine learning interatomic potentials.""",
    },
        {
        "name": "Daniel (Dan) Palmer",
        "position": "Graduate Student",
        "image": "profile-placeholder.gif",
        "description": """Dan is working on total energy tight binding models.""",
    },
    {
        "name": "Doruk Uçar",
        "position": "Graduate Student",
        "image": "profile-placeholder.gif",
        "description": """Doruk is working on uncertainty quantification.""",
    },

        {
        "name": "Shubhang Goswani",
        "position": "Graduate Student",
        "image": "goswami.jpg",
        "description": """Shubhang is working on learning hydrogen models.""",
    },
  {
        "name": "Sonali Joshi",
        "position": "Graduate Student",
        "image": "Sonali_photo.jpg",
        "description": """Sonali is working on automated learning of quantum models from ab initio calculations.""",
    },
      {
        "name": "Rohan Joshi",
        "position": "Graduate Student",
        "image": "rohan.jpg",
        "description": """Rohan is working on interactions in 2D materials.""",
    },
]


alumni = [
        {
        "name": "Andriy Nevidomskyy",
        "position": "co-PI",
        "image": "andriy.jpg",
        "description": """Correlated lattice models""",
    },
        {
        "name": "Kittithat (Mick) Krongchon",
        "position": "Graduate Student",
        "image": "mick.jpg",
        "description": """Mick is working on van der Waals interactions in 2D systems.
 """,
    },
    {
        "name": "Matthew Turk",
        "position": "co-PI",
        "image": "turk.jpg",
        "description": """yt, visualization""",
    },
        {
        "name": "Scott Jensen",
        "position": "Postdoctoral Associate",
        "image": "Jensen_pic.png",
        "description": """Hydrogen and 2D electron gas.""",
    },
        {
        "name": "Yueqing Chang",
        "position": "Graduate Student",
        "image": "yueqing.jpg",
        "description": """Learning emergent models from ab initio calculations. She graduated in 2022 and moved on to a postdoc at Rutgers.
 """},
         {
        "name": "Shivesh Pathak",
        "position": "Graduate Student",
        "image": "shivesh.png",
        "description": """Learning emergent models from ab initio calculations. He graduated in 2021 and moved on to a postdoc at Sandia National Labs.
 """},
     {
        "name": "Kevin Ly",
        "position": "Graduate Student",
        "image": "profile-placeholder.gif",
        "description": """Kevin is working on learning hydrogen models.""",
    },

]

print(
    """---
layout: page
title: Group members
permalink: /group/
---

## Current

<table cellpadding="5" border="0" style="width:100%">
<tbody>
"""
)
for m in members:
    print(member_format(m))

print(
    """
</tbody>
</table>
"""
)

print(
    """## Alumni

<table cellpadding="5" border="0" style="width:100%">
<tbody>
"""
)
for a in alumni:
    print(member_format(a))
print(
    """
</tbody>
</table>
"""
)
