// pages/team_more/team_more.js
var app=getApp();

Page({
  /**
   * 页面的初始数据
   */
  data: {
    team: { id: 321, count: 3, sup: 5, leader: "张一一", info: "这是一个神秘的队伍这是一个神秘的队伍这是一个神秘的队伍这是一个神秘的队伍这是一个神秘的队伍", member: ["张一一", "张二二", "张三三"] },
  },
  //加入队伍
  join_team: function(e){
    wx.request({
      url: ' ',//在这里加上后台的php地址
      data: { //发送给后台的数据
        'class_id': app.globalData.class_id,
        'team_id': app.globalData.team_id,
        'student_id': app.globalData.student_id
      },
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res.data里面要有state、info、class_info,teams（页面主要数据），如果成功就在info里说成功，下面的弹窗会提醒,不成功给出错误信息info。
        if (res.data.state == 1) { //用php返回的数据更新页面数据
          wx.showToast({
            title: res.data.info
          });
          wx.navigateTo({ //跳转回班级首页
            url: '../team_list/team_list',
          });
        } else {
          wx.showToast({
            title: res.data.info
          });
        }
      }
    });
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: ' ',//在这里加上后台的php地址
      data: { //发送给后台的数据
        'team_id': app.globalData.team_id,
      },
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res.data里面要有state、info、team_info，如果成功就在info里说成功，下面的弹窗会提醒,不成功给出错误信息info。
        if (res.data.state == 1) { //用php返回的数据更新页面数据
          this.setData({ team: res.data.team_info })
        } else {
          wx.showToast({
            title: res.data.info
          });
        }
      }
    });
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})