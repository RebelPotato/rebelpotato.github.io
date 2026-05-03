---
title: A Simple Knot-Drawing Algorithm
en: true
created-on: 2026-05-03
updated-on: 2026-05-03
---

I think all the [knot drawing attempts](celtic-knots-resources/index.md) that I collected use this algorithm. Follow these steps:

1. Tile the plane using polygons you like.
2. Label each edge as either a wall, a crossing or a hole.
3. For each edge, draw: a path parallel to it if it's a wall, a cross if it's a crossing, and two parallel paths coming through if it's an edge.
4. Walk around each polygon and connect loose ends between adjacent edges. Make sure that no paths cross within a polygon.

Congratulations, you've just made your very own knot! It's pretty simple and clear once you've used it to draw a knot in action. The two knot-making fonts are just special cases of this algorithm by restricting the tiling to a square tiling.

This seems quite OK to implement on a computer...
