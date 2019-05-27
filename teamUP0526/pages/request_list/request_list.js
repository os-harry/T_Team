// pages/request_list/request_list.js
var app=getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    invite_data: [{ id: 0, cap: "队长", team_id: "002", member: ["aaa", "hhh"], time: "2019-05-20 13:14", me: "me", read: true }, { id: 1, cap: "队长2", team_id: "003", member: ["rrr", "hhh"], time: "2019-05-20 13:17", me: "gaga", read: false }, { id: 2, cap: "队长4", team_id: "004", member: ["rrr", "hhh"], time: "2019-05-20 13:19", me: "gaaga", read: true }, { id: 3, cap: "队长2", team_id: "003", member: ["rrr", "hhh"], time: "2019-05-20 13:17", me: "gaga" ,read:false}]
  },

  read_more: function(e){
    app.globalData.invite_msg_id = e.currentTarget.dataset.msg_id //修改公共的msg_id值
    console.log('传入的消息id为：', e.currentTarget.dataset.msg_id)
    wx.navigateTo({  //页面跳转
      url: '../request_more/request_more',
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: ' ',//在这里加上后台的php地址
      data: { //发送给后台的数据
        'student_id': app.globalData.student_id,
      },
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res.data里面要有state、info、invite_data（页面主要数据），如果成功就在info里说成功，下面的弹窗会提醒,不成功给出错误信息info。
        if (res.data.state == 1) { //用php返回的数据更新页面数据
          this.setData({ invite_data: res.data.invite_data })
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