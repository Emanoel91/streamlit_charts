import streamlit as st
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node=dict(
      pad=15,
      thickness=20,
      line=dict(color="black", width=0.5),
      label=["Osmosis","Fantom","BNB Chain","Base","Optimism","Polygon","Arbitrum","Terra","Ethereum","Celo","Avalanche"],
      color=["#ff00ff","#00aaff","#ffc800","#0055ff","#ff0000","#aa00ff","#00d4ff","#ffe100","#bfbfbf","#00c48f","#ff2222"]
    ),
    link=dict(
      source=[0,0,1,1,2,2,3,4,5,6,7,8],
      target=[8,6,6,5,5,2,2,3,1,0,9,10],
      value=[8,4,2,8,4,2,6,2,1,4,3,5]
  ))])

st.plotly_chart(fig)
